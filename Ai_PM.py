import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="💼 AI-Driven Portfolio Management Tool",
    page_icon="💼",
    layout="wide"
)

# Background Image
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1506748686214-e9df14d4d9d9");
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.title("AI-Driven Portfolio Management Tool")

# Sidebar with Gradient Background
st.sidebar.title("User Input")
st.sidebar.markdown("---")

# User Input - Risk Profile
risk_profile = st.sidebar.selectbox(
    "Select Your Risk Profile:",
    ("Low Risk", "Medium Risk", "High Risk")
)

# User Input - Financial Goals
financial_goals = st.sidebar.number_input(
    "Enter Your Financial Goals ($)",
    min_value=0,
    step=1000
)

# User Input - Market Conditions
market_conditions = st.sidebar.slider(
    "Market Conditions (1-10, 1 being worst, 10 being best):",
    min_value=1,
    max_value=10,
    value=5
)

# Button to Generate Portfolio with Gradient Background
if st.sidebar.button("Generate Portfolio"):
    # Display User Input Summary
    st.subheader("User Input Summary")
    st.write(f"**Risk Profile:** {risk_profile}")
    st.write(f"**Financial Goals:** ${financial_goals}")
    st.write(f"**Market Conditions:** {market_conditions}/10")

    # Placeholder for Portfolio Generation Logic
    # Display Portfolio Summary
    st.subheader("Generated Portfolio Summary")
    st.write("Based on your inputs, it's recommended to allocate your portfolio as follows:")

    if risk_profile == "Low Risk":
        bonds_percentage = 60
        bonds_amount = financial_goals * bonds_percentage / 100
        st.write(f"- {bonds_percentage}% in bonds or fixed-income securities (${bonds_amount:.2f})")

        stocks_percentage = 30
        stocks_amount = financial_goals * stocks_percentage / 100
        st.write(f"- {stocks_percentage}% in blue-chip stocks (${stocks_amount:.2f})")

        cash_percentage = 10
        cash_amount = financial_goals * cash_percentage / 100
        st.write(f"- {cash_percentage}% in cash or cash equivalents (${cash_amount:.2f})")

    elif risk_profile == "Medium Risk":
        # Similar logic for medium risk profile
        pass

    elif risk_profile == "High Risk":
        # Similar logic for high risk profile
        pass

    # Placeholder for AI-driven portfolio recommendations
    # Display AI-driven recommendations based on user input and market data
    st.subheader("AI-driven Portfolio Recommendations")
    st.write("Based on your inputs and current market conditions, our AI model suggests the following strategies:")

    if market_conditions >= 7:
        st.write("- Consider allocating more to equities due to favorable market conditions.")
        st.write("- Focus on growth-oriented assets to capitalize on market momentum.")

    elif market_conditions <= 4:
        st.write("- Allocate more to fixed-income securities or defensive stocks to mitigate risk.")
        st.write("- Consider diversifying into alternative assets such as gold or real estate.")

    else:
        st.write("- Maintain a balanced portfolio with a mix of equities and fixed-income securities.")
        st.write("- Regularly review and rebalance your portfolio to adapt to changing market conditions.")
