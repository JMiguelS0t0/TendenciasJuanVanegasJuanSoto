import axios from "axios";

export const addInsurance = async (newInsuranceData) => {
    try {
        const response = await axios.post(
            "http://127.0.0.1:8000/hospital/insurance",
            newInsuranceData
        );
        return response.data;
    } catch (error) {
        if (error.response && error.response.data) {
            console.error("Error creating contact data: ", error.response.data);
            throw new Error(error.response.data.message || "Unknown server error");
        } else {
            console.error("Error creating contact data: ", error);
            throw new Error(error.message || "Unknown error");
        }
    }
};