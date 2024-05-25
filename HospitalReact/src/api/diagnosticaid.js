import axios from 'axios';

export const getDiagnosticaids = async () => {
    try {
        const response = await axios.get('http://127.0.0.1:8000/hospital/support/diagnosticaid');
        return response.data;
    } catch (error) {
        console.log("Error getting data of diagnosticaids: ", error);
        throw error;
    }
}

export const addDiagnosticaid = async (data) => {
    try {
        const response = await axios.post('http://127.0.0.1:8000/hospital/support/diagnosticaid', data);
        return response.data;
    } catch (error) {
        if (error.response && error.response.data) {
            throw new Error(error.response.data || "Unknown server error");
        } else {
            console.log("Error creating medication data: ", error);
            throw new Error(error.message || "Unknown server error");
        }
    }
};

export const updateDiagnosticaid = async (id, data) => {
    try {
        const response = await axios.put(`http://127.0.0.1:8000/hospital/support/diagnosticaid/${id}`, data)
        return response.data;
    } catch (error) {
        if (error.response && error.response.data) {
            console.log("Error updating person data: ", error.response.data);
            throw new Error(error.response.data.message || "Unknown server error");
        } else {
            console.log("Error updating person data: ", error);
            throw new Error(error.message || "Unknown error");
        }
    }
};

export const deleteDiagnosticaid = async (id) => {
    try {
        const response = await axios.delete(
            `http://127.0.0.1:8000/hospital/support/diagnosticaid/${id}`
        );
        return response.data;
    } catch (error) {
        if (error.response && error.response.data) {
            console.log("Error deleting person data: ", error.response.data);
            throw new Error(error.response.data.message || "Unknown server error");
        } else {
            console.log("Error deleting person data: ", error);
            throw new Error(error.message || "Unknown error");
        }
    }
};