import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="AI-Driven Portfolio Management Tool",
    page_icon="💼",
    layout="wide"
)

# Background Image
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://www.nerdwallet.com/assets/blog/wp-content/uploads/2019/09/GettyImages-639106078.jpg-what-is-portfolio-management.jpg");
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
        stocks_percentage = 50
        stocks_amount = financial_goals * stocks_percentage / 100
        st.write(f"- {stocks_percentage}% in diversified stocks (${stocks_amount:.2f})")

        bonds_percentage = 30
        bonds_amount = financial_goals * bonds_percentage / 100
        st.write(f"- {bonds_percentage}% in bonds or fixed-income securities (${bonds_amount:.2f})")

        reits_percentage = 15
        reits_amount = financial_goals * reits_percentage / 100
        st.write(f"- {reits_percentage}% in real estate investment trusts (REITs) (${reits_amount:.2f})")

        cash_percentage = 5
        cash_amount = financial_goals * cash_percentage / 100
        st.write(f"- {cash_percentage}% in cash or cash equivalents (${cash_amount:.2f})")

    elif risk_profile == "High Risk":
        growth_stocks_percentage = 60
        growth_stocks_amount = financial_goals * growth_stocks_percentage / 100
        st.write(f"- {growth_stocks_percentage}% in growth stocks (${growth_stocks_amount:.2f})")

        emerging_markets_percentage = 20
        emerging_markets_amount = financial_goals * emerging_markets_percentage / 100
        st.write(f"- {emerging_markets_percentage}% in emerging market funds (${emerging_markets_amount:.2f})")

        tech_etfs_percentage = 15
        tech_etfs_amount = financial_goals * tech_etfs_percentage / 100
        st.write(f"- {tech_etfs_percentage}% in technology sector ETFs (${tech_etfs_amount:.2f})")

        speculative_investments_percentage = 5
        speculative_investments_amount = financial_goals * speculative_investments_percentage / 100
        st.write(f"- {speculative_investments_percentage}% in speculative investments or individual stocks (${speculative_investments_amount:.2f})")

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
