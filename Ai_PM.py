import streamlit as st

# Page Title with Icon
st.title("📈 AI-Driven Portfolio Management Tool")

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
        st.write("- 60% in bonds or fixed-income securities")
        st.write("- 30% in blue-chip stocks")
        st.write("- 10% in cash or cash equivalents")

    elif risk_profile == "Medium Risk":
        st.write("- 40% in diversified stocks")
        st.write("- 30% in bonds or fixed-income securities")
        st.write("- 20% in real estate investment trusts (REITs)")
        st.write("- 10% in cash or cash equivalents")

    elif risk_profile == "High Risk":
        st.write("- 50% in growth stocks")
        st.write("- 20% in emerging market funds")
        st.write("- 20% in technology sector ETFs")
        st.write("- 10% in speculative investments or individual stocks")

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
