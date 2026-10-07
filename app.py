import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# Model was saved with scikit-learn 1.6.1.
MODEL_PATH = Path(__file__).parent / "upi_fraud_model(6).pkl"

@st.cache_resource
def load_model():
    if not MODEL_PATH.exists():
        st.error(f"Model file not found: {MODEL_PATH.name}")
        st.stop()

    try:
        return joblib.load(MODEL_PATH)
    except Exception as e:
        st.error("The saved UPI model could not be loaded.")
        st.code(str(e))
        st.info(
            "This model requires the same compatible scikit-learn environment "
            "used when it was saved. Use scikit-learn==1.6.1 in requirements.txt "
            "and redeploy the Streamlit app."
        )
        st.stop()

model = load_model()

st.set_page_config(
    page_title="UPI Fraud Detection",
    page_icon="🛡️",
    layout="centered"
)

st.title("🛡️ UPI Fraud Detection System")
st.write("Enter transaction details to estimate the fraud risk.")

transaction_amount = st.number_input(
    "Transaction Amount (₹)", min_value=1.0, value=1000.0
)

transaction_hour = st.slider(
    "Transaction Hour", min_value=0, max_value=23, value=12
)

device_type = st.selectbox(
    "Device Type", ["Android", "iOS", "Web"]
)

location_changed = st.selectbox(
    "Location Changed?", [0, 1],
    format_func=lambda x: "Yes" if x == 1 else "No"
)

previous_failed_transactions = st.number_input(
    "Previous Failed Transactions", min_value=0, value=0
)

transactions_last_24h = st.number_input(
    "Transactions in Last 24 Hours", min_value=0, value=3
)

account_age_days = st.number_input(
    "Account Age (Days)", min_value=1, value=500
)

merchant_category = st.selectbox(
    "Merchant Category",
    ["Shopping", "Food", "Travel", "Bills", "Education", "Other"]
)

average_transaction_amount = st.number_input(
    "Average Transaction Amount (₹)", min_value=1.0, value=1000.0
)

if st.button("🔍 Check Transaction", use_container_width=True):

    amount_deviation = (
        transaction_amount / (average_transaction_amount + 1)
    )

    is_night = int(
        transaction_hour <= 4 or transaction_hour >= 23
    )

    high_transaction_activity = int(
        transactions_last_24h >= 10
    )

    failed_transaction_flag = int(
        previous_failed_transactions >= 3
    )

    transaction = pd.DataFrame({
        "transaction_amount": [transaction_amount],
        "transaction_hour": [transaction_hour],
        "device_type": [device_type],
        "location_changed": [location_changed],
        "previous_failed_transactions": [previous_failed_transactions],
        "transactions_last_24h": [transactions_last_24h],
        "account_age_days": [account_age_days],
        "merchant_category": [merchant_category],
        "average_transaction_amount": [average_transaction_amount],
        "amount_deviation": [amount_deviation],
        "is_night": [is_night],
        "high_transaction_activity": [high_transaction_activity],
        "failed_transaction_flag": [failed_transaction_flag]
    })

    try:
        prediction = model.predict(transaction)[0]
        probability = model.predict_proba(transaction)[0][1]
    except Exception as e:
        st.error("Prediction failed.")
        st.code(str(e))
        st.stop()

    if probability < 0.30:
        risk = "Low Risk"
    elif probability < 0.70:
        risk = "Medium Risk"
    else:
        risk = "High Risk"

    st.divider()
    st.subheader("Prediction")

    if prediction == 1:
        st.error("🚨 Potential Fraud Detected")
    else:
        st.success("✅ Transaction Appears Legitimate")

    st.metric(
        "Fraud Probability",
        f"{probability * 100:.2f}%"
    )

    st.write(f"**Risk Level:** {risk}")
