import streamlit as st
import requests

# 1. Page Configuration

st.set_page_config(
    page_title="FraudCheck AI | Claim Analyzer",
    layout="centered" # Changed to 'centered' so the pages look like a neat form
)

# 2. Title & Header

st.title("FraudCheck AI: Vehicle Insurance Claim Analyzer")
st.markdown("Please fill out the information in each step below, then proceed to the final step to run the analysis.")
st.markdown("---")

# 3. Create Multi-Page Tabs (The Step-by-Step Wizard)

tab1, tab2, tab3, tab4 = st.tabs([
    "Step 1: Policy & Customer", 
    "Step 2: Vehicle Info", 
    "Step 3: Incident Details", 
    "Step 4: Run Analysis"
])

# --- PAGE / TAB 1: Policy & Customer Profile ---
with tab1:
    st.header("Step 1: Policy & Customer Information")
    
    col_a, col_b = st.columns(2)
    with col_a:
        Month = st.selectbox("Month of Accident", ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
        WeekOfMonth = st.number_input("Week of Month", 1, 5, 1)
        DayOfWeek = st.selectbox("Day of Week", ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'])
        Sex = st.selectbox("Sex", ["Male", "Female"])
        Age = st.number_input("Driver Age", 16, 100, 30)
    with col_b:
        MaritalStatus = st.selectbox("Marital Status", ["Single","Married","Widow","Divorced"])
        AgeOfPolicyHolder = st.selectbox("Age of Policy Holder", ["16 to 17","18 to 20","21 to 25","26 to 30","31 to 35","36 to 40","41 to 50","51 to 65","over 65"])
        BasePolicy = st.selectbox("Base Policy", ["Liability","Collision","All Perils"])
        PolicyType = st.selectbox("Policy Type", ["Sport - Liability","Sport - Collision","Sedan - Liability","Sedan - All Perils","Sedan - Collision","Utility - All Perils","Utility - Liability","Utility - Collision","Sport - All Perils"])


# --- PAGE / TAB 2: Vehicle Information ---
with tab2:
    st.header("Step 2: Vehicle Information")
    
    col_c, col_d = st.columns(2)
    with col_c:
        Make = st.selectbox("Vehicle Make", ["Honda","Toyota","Ford","Mazda","Chevrolet","Pontiac","Accura","Dodge","Mercury","Jaguar","Nisson","VW","Saab","Saturn","Porche","BMW","Ferrari","Lexus"])
        VehicleCategory = st.selectbox("Vehicle Category", ["Sport","Sedan","Utility"])
        VehiclePrice = st.selectbox("Vehicle Price Range", ["less than 20,000","20,000 to 29,000","30,000 to 39,000","40,000 to 59,000","60,000 to 69,000","more than 69,000"])
    with col_d:
        AgeOfVehicle = st.selectbox("Age of Vehicle", ["new","2 years","3 years","4 years","5 years","6 years","7 years","more than 7"])
        Year = st.number_input("Vehicle Year", 1990, 2026, 1994)
        NumberOfCars = st.selectbox("Number of Cars under Policy", ["1 vehicle","2 vehicles","3 to 4","5 to 8","more than 8"])


# --- PAGE / TAB 3: Incident & Claim Details ---
with tab3:
    st.header("Step 3: Incident & Claim Details")
    
    col_e, col_f = st.columns(2)
    with col_e:
        AccidentArea = st.selectbox("Accident Area", ["Urban","Rural"])
        Fault = st.selectbox("Who is at Fault?", ["Policy Holder","Third Party"])
        MonthClaimed = st.selectbox("Month Claimed", ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
        WeekOfMonthClaimed = st.number_input("Week Claimed", 1, 5, 1)
        DayOfWeekClaimed = st.selectbox("Day Claimed", ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'])
        Deductible = st.number_input("Deductible Amount", 100, 1000, 400, 100)
        DriverRating = st.number_input("Driver Rating (1-4)", 1, 4, 1)
    with col_f:
        Days_Policy_Accident = st.selectbox("Days from Policy to Accident", ["none", "1 to 7", "8 to 14", "15 to 30", "more than 30"])
        Days_Policy_Claim = st.selectbox("Days from Policy to Claim", ["none", "1 to 7", "8 to 14", "15 to 30", "more than 30"])
        PastNumberOfClaims = st.selectbox("Past Number of Claims", ["none", "1", "2 to 4", "more than 4"])
        AddressChange_Claim = st.selectbox("Address Change after Claim", ["no change", "under 6 months", "1 year", "2 to 3 years", "4 to 8 years"])
        PoliceReportFiled = st.selectbox("Police Report Filed?", ["No","Yes"])
        WitnessPresent = st.selectbox("Witness Present?", ["No","Yes"])
        AgentType = st.selectbox("Agent Type", ["External", "Internal"])
        NumberOfSuppliments = st.selectbox("Number of Supplements", ["none", "1 to 2", "3 to 5", "more than 5"])


# --- PAGE / TAB 4: Analysis & API Call ---
with tab4:
    st.header("Step 4: Execute Machine Learning Analysis")
    st.markdown("Please ensure all data in Steps 1 through 3 is correct before proceeding.")
    st.markdown("<br>", unsafe_allow_html=True)
    
    analyze_button = st.button("Run Fraud Analysis Model", use_container_width=True)

    if analyze_button:
        # Gather all inputs into the dictionary (Streamlit remembers the data from the other tabs automatically)
        payload = {
            "Month": Month, "WeekOfMonth": WeekOfMonth, "DayOfWeek": DayOfWeek,
            "Make": Make, "AccidentArea": AccidentArea, "DayOfWeekClaimed": DayOfWeekClaimed,
            "MonthClaimed": MonthClaimed, "WeekOfMonthClaimed": WeekOfMonthClaimed,
            "Sex": Sex, "MaritalStatus": MaritalStatus, "Age": Age, "Fault": Fault,
            "PolicyType": PolicyType, "VehicleCategory": VehicleCategory, "VehiclePrice": VehiclePrice,
            "Deductible": Deductible, "DriverRating": DriverRating,
            "Days_Policy_Accident": Days_Policy_Accident, "Days_Policy_Claim": Days_Policy_Claim,
            "PastNumberOfClaims": PastNumberOfClaims, "AgeOfVehicle": AgeOfVehicle,
            "AgeOfPolicyHolder": AgeOfPolicyHolder, "PoliceReportFiled": PoliceReportFiled,
            "WitnessPresent": WitnessPresent, "AgentType": AgentType,
            "NumberOfSuppliments": NumberOfSuppliments, "AddressChange_Claim": AddressChange_Claim,
            "NumberOfCars": NumberOfCars, "Year": Year, "BasePolicy": BasePolicy
        }

        API_URL = "http://127.0.0.1:8000/predict"

        try:
            with st.spinner("Connecting to API and executing model..."):
                response = requests.post(API_URL, json=payload)

            if response.status_code == 200:
                result = response.json()
                prediction = result["prediction"]
                probability = result["fraud_probability_percentage"]

                st.markdown("### Analysis Results")
                if prediction == "Fraud":
                    st.error(f"Potential Fraud Detected. The model indicates a {probability}% probability that this claim is fraudulent.")
                else:
                    st.success(f"Claim Looks Legitimate. The model indicates a low fraud probability ({probability}%).")

            else:
                st.error(f"API Error: {response.text}")

        except Exception as e:
            st.error("Cannot connect to API. Please ensure your FastAPI server (`API.py`) is running on port 8000.")