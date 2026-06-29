import streamlit as st
import io
from utils.pdf_processor import extract_text_from_pdf
from utils.vector_store import create_vector_store
from utils.summarizer import summarize_text
from utils.qa_engine import build_qa_chain, answer_question
from utils.keywords import extract_keywords, extract_topics

# ✅ Page Config
st.set_page_config(
    page_title="ResearchGPT",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ✅ Custom CSS for Modern Look
st.markdown("""
    <style>
    /* Gradient Title */
    .title {
        font-size: 40px;
        font-weight: bold;
        background: -webkit-linear-gradient(45deg, #6a11cb, #2575fc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 20px;
    }

    /* Glassmorphism Card */
    .card {
        background: rgba(255, 255, 255, 0.15);
        border-radius: 15px;
        padding: 20px;
        backdrop-filter: blur(10px);
        box-shadow: 0 4px 30px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }

    /* Tabs Styling */
    .stTabs [role="tablist"] {
        justify-content: center;
    }
    .stTabs [role="tab"] {
        font-weight: bold;
        color: #2575fc;
    }

    /* Buttons Hover */
    .stDownloadButton button:hover {
        background-color: #2575fc !important;
        color: white !important;
        transform: scale(1.05);
        transition: 0.3s;
    }
    </style>
""", unsafe_allow_html=True)

# ✅ Gradient Title
st.markdown('<div class="title">📄 ResearchGPT — AI Research Paper Assistant</div>', unsafe_allow_html=True)

uploaded_file = st.file_uploader("📂 Upload a Research Paper (PDF)", type="pdf")

if uploaded_file:
    with st.spinner("📖 Reading PDF..."):
        raw_text = extract_text_from_pdf(uploaded_file)
    st.success("✅ PDF loaded successfully!")

    # Build vector store once
    if "vector_store" not in st.session_state:
        with st.spinner("⚡ Building knowledge base..."):
            st.session_state.vector_store = create_vector_store(raw_text)
            st.session_state.qa_chain = build_qa_chain(st.session_state.vector_store)

    tab1, tab2, tab3, tab4 = st.tabs(["📝 Summary", "🔑 Keywords", "🧠 Topics", "💬 Ask Questions"])

    # ✅ TAB 1 - Summary
    with tab1:
        if "summary" not in st.session_state:
            with st.spinner("✨ Generating summary..."):
                st.session_state.summary = summarize_text(raw_text)

        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("📝 Paper Summary")
        st.write(st.session_state.summary)
        st.markdown('</div>', unsafe_allow_html=True)

        # Download Buttons
        txt_bytes = io.BytesIO(st.session_state.summary.encode("utf-8"))
        st.download_button("⬇️ Download Summary as TXT", txt_bytes, "summary.txt", "text/plain")

        try:
            from fpdf import FPDF
            def generate_pdf(text):
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", size=12)
                for line in text.split('\n'):
                    pdf.multi_cell(0, 10, line)
                return pdf.output(dest='S').encode('latin-1')

            pdf_bytes = generate_pdf(st.session_state.summary)
            st.download_button("⬇️ Download Summary as PDF", pdf_bytes, "summary.pdf", "application/pdf")
        except ImportError:
            st.info("⚠️ Install fpdf to enable PDF download: `pip install fpdf`")

    # ✅ TAB 2 - Keywords
    with tab2:
        if "keywords" not in st.session_state:
            st.session_state.keywords = extract_keywords(raw_text)

        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("🔑 Top Keywords")
        cols = st.columns(5)
        for i, kw in enumerate(st.session_state.keywords):
            cols[i % 5].markdown(f"<span style='color:#6a11cb; font-weight:bold;'>`{kw}`</span>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # ✅ TAB 3 - Topics
    with tab3:
        if "topics" not in st.session_state:
            st.session_state.topics = extract_topics(raw_text)

        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("🧠 Detected Topics")
        if st.session_state.topics:
            for topic in st.session_state.topics:
                st.markdown(f"- {topic}")
        else:
            st.info("No significant topics detected.")
        st.markdown('</div>', unsafe_allow_html=True)

   