import axios from 'axios';

export const getProcedures = async () => {
    try {
        const response = await axios.get('http://127.0.0.1:8000/hospital/support/procedure');
        return response.data;
    } catch (error) {
        console.log("Error getting data of procedures: ", error);
        throw error;
    }
}

export const addProcedure = async (data) => {
    try {
        const response = await axios.post('http://127.0.0.1:8000/hospital/support/procedure', data);
        return response.data;
    } catch (error) {
        if (error.response && error.response.data) {
            throw new Error(error.response.data || "Uknown server error");
        } else {
            console.log("Error adding procedure: ", error);
            throw new Error(error.message || "Uknown server error");
        }
    }
}

export const updateProcedure = async (id, data) => {
    try {
        const response = await axios.put(`http://127.0.0.1:8000/hospital/support/procedure/${id}`, data);
        return response.data;
    } catch (error) {
        if (error.response && error.response.data) {
            throw new Error(error.response.data || "Uknown server error");
        } else {
            console.log("Error updating procedure: ", error);
            throw new Error(error.message || "Uknown server error");
        }
    }
}

export const deleteProcedure = async (id) => {
    try {
        const response = await axios.delete(`http://127.0.0.1:8000/hospital/support/procedure/${id}`);
        return response.data;
    } catch (error) {
        if (error.response && error.response.data) {
            throw new Error(error.response.data || "Uknown server error");
        } else {
            console.log("Error deleting procedure: ", error);
            throw new Error(error.message || "Uknown server error");
        }
    }
}