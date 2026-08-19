from __future__ import annotations

from pathlib import Path

import streamlit as st
from markitdown import MarkItDown

from converter import SUPPORTED_EXTENSIONS, convert_bytes

APP_TITLE = "MarkItDown File Converter"
APP_DESCRIPTION = (
    "Upload a file, convert it to Markdown with MarkItDown, and copy the result into ChatGPT."
)

SUPPORTED_UPLOAD_EXTENSIONS = sorted(
    extension.removeprefix(".") for extension in SUPPORTED_EXTENSIONS
)


@st.cache_resource
def get_converter() -> MarkItDown:
    return MarkItDown()


def convert_upload(uploaded_file) -> tuple[str, str]:
    """Convert an uploaded file to Markdown and return (markdown, source_name)."""

    markdown = convert_bytes(
        uploaded_file.name,
        uploaded_file.getvalue(),
        converter=get_converter(),
    )
    return markdown, uploaded_file.name


st.set_page_config(page_title=APP_TITLE, page_icon="📝", layout="wide")

st.title(APP_TITLE)
st.write(APP_DESCRIPTION)

if "last_markdown" not in st.session_state:
    st.session_state.last_markdown = ""
if "last_source_name" not in st.session_state:
    st.session_state.last_source_name = ""

with st.sidebar:
    st.subheader("How to use")
    st.markdown(
        """
1. Upload a file.
2. Wait for conversion.
3. Copy or download the Markdown.

This app uses `convert_local()` so it only processes the file you upload.
        """.strip()
    )
    st.subheader("Supported file types")
    st.caption(", ".join(SUPPORTED_UPLOAD_EXTENSIONS))

uploaded_file = st.file_uploader(
    "Choose a file",
    type=SUPPORTED_UPLOAD_EXTENSIONS,
    help="Any file MarkItDown can handle locally.",
)

if uploaded_file is not None:
    st.write(f"Selected: `{uploaded_file.name}`")
    st.write(f"Size: {uploaded_file.size:,} bytes")

    if st.button("Convert to Markdown", type="primary"):
        with st.spinner("Converting..."):
            try:
                markdown, source_name = convert_upload(uploaded_file)
            except Exception as exc:  # noqa: BLE001
                st.error(f"Conversion failed: {exc}")
                st.stop()

        st.session_state.last_markdown = markdown
        st.session_state.last_source_name = source_name
elif not st.session_state.last_markdown:
    st.info("Upload a file to generate Markdown.")

if st.session_state.last_markdown:
    markdown = st.session_state.last_markdown
    source_name = st.session_state.last_source_name

    if not markdown.strip():
        st.warning("MarkItDown returned no text for this file.")
    else:
        st.success("Conversion complete.")
        st.write(f"Source: `{source_name}`")
        st.text_area("Markdown output", markdown, height=600)
        st.download_button(
            "Download Markdown",
            data=markdown.encode("utf-8"),
            file_name=f"{Path(source_name).stem}.md",
            mime="text/markdown",
        )
elif uploaded_file is not None:
    st.caption("Click Convert to Markdown to generate the output.")
