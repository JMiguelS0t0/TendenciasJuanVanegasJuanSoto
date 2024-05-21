import axios from "axios";

export const getMedications = async () => {
  try {
    const response = await axios.get(
      "http://127.0.0.1:8000/hospital/support/medication"
    );
    return response.data;
  } catch (error) {
    console.error("Error getting medicines: ", error);
    throw error;
  }
};

export const addMedication = async (newMedicationData) => {
  try {
    const response = await axios.post(
      "http://127.0.0.1:8000/hospital/support/medication",
      newMedicationData
    );
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

export const updateMedicationData = async (id, updateData) => {
  try {
    const response = await axios.put(
      `http://127.0.0.1:8000/hospital/support/medication/${id}`,
      updateData
    );
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

export const deleteMedicine = async (id) => {
  try {
    const response = await axios.delete(
      `http://127.0.0.1:8000/hospital/support/medication/${id}`
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
