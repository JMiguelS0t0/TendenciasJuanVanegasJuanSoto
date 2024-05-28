import axios from "axios";

export const fetchPatientData = async (id = null) => {
    try {
        let url = "http://127.0.0.1:8000/hospital/patient";
        if (id) {
            url += `/${id}`;
        }
        const response = await axios.get(url);
        return response.data;
    } catch (error) {
        console.error("Error fetching person data: ", error);
        throw error;
    }
};

export const createPatientData = async (newPatientData) => {
    try {
        const response = await axios.post(
            "http://127.0.0.1:8000/hospital/patient",
            newPatientData
        );
        return response.data;
    } catch (error) {
        if (error.response && error.response.data) {
            console.error("Error creating patient data: ", error.response.data);
            throw new Error(error.response.data.message || "Unknown server error");
        } else {
            console.error("Error creating patient data: ", error);
            throw new Error(error.message || "Unknown error");
        }
    }
};