import streamlit as st
from PIL import Image
import base64
import time
import os

# Page configuration
st.set_page_config(
    page_title="CHAI COPY - Coming Soon!",
    page_icon="☕",
    layout="wide",
)

# Function to load and encode local image
def load_local_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as image_file:
            encoded_image = base64.b64encode(image_file.read()).decode()
            return f"data:image/png;base64,{encoded_image}"
    return None

# Load local image
logo_path = "1735559911967.png"  # Replace with your actual image filename
logo_data = load_local_image(logo_path)

# Enhanced CSS with 3D effects, animations, and modern styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
    
    /* Modern scroll styling */
    ::-webkit-scrollbar {
        width: 10px;
        background: transparent;
    }
    
    ::-webkit-scrollbar-thumb {
        background: rgba(244, 164, 96, 0.5);
        border-radius: 5px;
    }
     /* Enhanced particles */
    .particle {
        position: absolute;
        background: linear-gradient(45deg, #F4A460, #8EA355);
        border-radius: 50%;
        width: 4px;
        height: 4px;
        filter: blur(1px);
    }
    .stApp {
        background: linear-gradient(135deg, #656B3F 0%, #4A4F2E 100%);
        perspective: 1000px;
    }
    
    .main-container {
        background: rgba(0, 0, 0, 0.2);
        border-radius: 20px;
        padding: 2rem;
        backdrop-filter: blur(10px);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.1);
        animation: fadeIn 1.5s ease-in-out;
        transform-style: preserve-3d;
        position: relative;
    }
    
    .main-container::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(45deg, rgba(255,255,255,0.1), transparent);
        transform: translateZ(-1px);
        border-radius: 20px;
    }
    
    @keyframes fadeIn {
        0% { opacity: 0; transform: translateY(20px) rotateX(10deg); }
        100% { opacity: 1; transform: translateY(0) rotateX(0); }
    }
    
    @keyframes float {
        0% { transform: translateY(0px) translateZ(20px) rotateY(0deg); }
        50% { transform: translateY(-10px) translateZ(50px) rotateY(10deg); }
        100% { transform: translateY(0px) translateZ(20px) rotateY(0deg); }
    }
    
    .logo-container {
        text-align: center;
        margin-bottom: 2rem;
        animation: float 6s ease-in-out infinite;
        transform-style: preserve-3d;
    }
    
    .logo-container img {
        width: 300px;
        height: auto;
        filter: drop-shadow(0 10px 15px rgba(0,0,0,0.2));
        transform: translateZ(50px);
        transition: transform 0.3s ease;
    }
    
    .logo-container img:hover {
        transform: translateZ(80px) scale(1.05);
    }
    
    .big-text {
        font-family: 'Poppins', sans-serif;
        font-size: 4.5rem !important;
        font-weight: 600 !important;
        text-align: center !important;
        background: linear-gradient(45deg, #8EA355 0%, #F4A460 100%);
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        transform: translateZ(30px);
    }
    
    .sub-text {
        font-family: 'Poppins', sans-serif;
        font-size: 2rem !important;
        text-align: center !important;
        color: #D4E6B5 !important;
        margin-top: 1rem !important;
        animation: fadeIn 2s ease-in-out;
        transform: translateZ(20px);
        text-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }
    
    .countdown {
        font-family: 'Poppins', sans-serif;
        font-size: 3rem !important;
        text-align: center !important;
        color: #F4A460 !important;
        margin-top: 2rem !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        animation: pulse 2s infinite;
        transform: translateZ(40px);
    }
    
    .location {
        font-family: 'Poppins', sans-serif;
        font-size: 1.5rem !important;
        text-align: center !important;
        color: #D4E6B5 !important;
        margin-top: 2rem !important;
        line-height: 2 !important;
        transform: translateZ(15px);
    }
    
    .location i {
        font-size: 1.8rem;
        margin-right: 0.5rem;
        color: #F4A460;
    }
    
    .email-container {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 15px;
        padding: 2rem;
        margin-top: 2rem;
        transform: translateZ(25px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }
    
    .stTextInput input {
        background: rgba(255, 255, 255, 0.1);
        border: 2px solid rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        color: #D4E6B5;
        padding: 1rem;
        font-family: 'Poppins', sans-serif;
        transform: translateZ(10px);
    }
    
    .stTextInput input:focus {
        border-color: #F4A460;
        box-shadow: 0 0 20px rgba(244, 164, 96, 0.3);
    }
    
    .stButton button {
        background: linear-gradient(45deg, #F4A460, #8EA355) !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 1rem 2rem !important;
        font-family: 'Poppins', sans-serif !important;
        transition: all 0.3s ease !important;
        transform: translateZ(20px);
    }
    
    .stButton button:hover {
        transform: translateZ(30px) translateY(-2px);
        box-shadow: 0 10px 25px rgba(0,0,0,0.2);
    }
    
    .social-links {
        margin-top: 2rem;
        padding: 1.5rem;
        border-top: 1px solid rgba(255,255,255,0.1);
        transform: translateZ(15px);
        background: rgba(255, 255, 255, 0.05);
        border-radius: 0 0 15px 15px;
    }
    
    .social-icon {
        font-size: 2rem;
        color: #F4A460;
        margin: 0 1rem;
        transition: all 0.3s ease;
    }
    
    .social-icon:hover {
        color: #8EA355;
        transform: translateY(-3px);
    }
    
    .progress-bar {
        height: 6px !important;
        background-color: rgba(255,255,255,0.1) !important;
        border-radius: 3px !important;
        transform: translateZ(5px);
    }
    
    .progress-bar > div {
        background: linear-gradient(45deg, #F4A460, #8EA355) !important;
        box-shadow: 0 0 10px rgba(244, 164, 96, 0.5);
    }
    
    /* Add particle effect */
    .particles {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: -1;
    }
    
    @keyframes particle-animation {
        0% {
            transform: translate(0, 0);
            opacity: 0;
        }
        50% {
            opacity: 0.5;
        }
        100% {
            transform: translate(var(--tx), var(--ty));
            opacity: 0;
        }
    }
    
    .particle {
        position: absolute;
        background: #F4A460;
        border-radius: 50%;
        width: 3px;
        height: 3px;
        animation: particle-animation 3s infinite;
    }
    </style>
    
    <!-- Add Font Awesome for better icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    
    <!-- Add particles -->
    <div class="particles" id="particles"></div>
    
    <script>
    function createParticles() {
        const container = document.querySelector('.particles');
        for (let i = 0; i < 50; i++) {
            const particle = document.createElement('div');
            particle.className = 'particle';
            particle.style.setProperty('--tx', Math.random() * 200 - 100 + 'px');
            particle.style.setProperty('--ty', Math.random() * 200 - 100 + 'px');
            particle.style.left = Math.random() * 100 + 'vw';
            particle.style.top = Math.random() * 100 + 'vh';
            container.appendChild(particle);
        }
    }
    
    // Call createParticles when the document is ready
    document.addEventListener('DOMContentLoaded', createParticles);
    </script>
    """, unsafe_allow_html=True)

# Create main container
st.markdown('<div class="main-container">', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,2,1])

with col2:
    # Enhanced logo container with 3D effect using local image
    if logo_data:
        st.markdown(f'''
            <div class="logo-container">
                <img src="{logo_data}" 
                     alt="CHAI COPY Logo"
                     style="transform-style: preserve-3d;">
            </div>
        ''', unsafe_allow_html=True)
    else:
        st.error("Logo image not found. Please check the image path.")
    
    # Enhanced tagline with modern icons
    st.markdown('''
        <div class="sub-text">
            <i class="fas fa-mug-hot"></i> Where Every Sip Tells a Story
        </div>
    ''', unsafe_allow_html=True)
    
    # Enhanced coming soon message
    st.markdown('''
        <div class="countdown">
            <i class="fas fa-store"></i> Opening Soon in Pilani!
        </div>
    ''', unsafe_allow_html=True)
    
    # Enhanced location details with modern icons
    st.markdown("""
        <div class="location">
            <i class="fas fa-home"></i> Your New Favorite Study Spot<br>
            <i class="fas fa-coffee"></i> Premium Tea • Artisanal Coffee • Vibrant Community<br>
            <i class="fas fa-sparkles"></i> A Perfect Blend of Calm & Creativity <i class="fas fa-sparkles"></i>
        </div>
    """, unsafe_allow_html=True)
    
    # Enhanced newsletter signup
    st.markdown("""
        <div class="email-container">
            <p style="color: #D4E6B5; font-size: 1.2rem; font-family: 'Poppins', sans-serif; text-align: center;">
                <i class="fas fa-envelope"></i> Be the first to know when we open our doors!
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Enhanced email signup with better layout
    email_col, button_col = st.columns([3,1])
    with email_col:
        email = st.text_input("", placeholder="Enter your email address", label_visibility="collapsed")
    with button_col:
        if st.button("Notify Me"):
            if email:
                st.success("🎉 Thanks for joining our journey! We'll keep you posted.")
    
    # Enhanced social media section
    st.markdown("""
        <div class="social-links">
            <p style="color: #D4E6B5; font-size: 1.2rem; font-family: 'Poppins', sans-serif; text-align: center;">
                <i class="fas fa-heart"></i> Follow our journey
            </p>
            <div style="text-align: center; margin-top: 1rem;">
                <a href="#" class="social-icon"><i class="fab fa-instagram"></i></a>
                <a href="#" class="social-icon"><i class="fab fa-facebook"></i></a>
                <a href="#" class="social-icon"><i class="fab fa-twitter"></i></a>
            </div>
        </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Enhanced loading animation
progress_bar = st.progress(0)
for i in range(100):
    time.sleep(0.01)
    progress_bar.progress(i + 1)