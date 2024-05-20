import axios from "axios";

export const fetchPersonData = async (id = null) => {
  try {
    let url = "http://127.0.0.1:8000/hospital/person";
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

export const createPersonData = async (newPersonData) => {
  try {
    const response = await axios.post(
      "http://127.0.0.1:8000/hospital/person",
      newPersonData
    );
    return response.data;
  } catch (error) {
    if (error.response && error.response.data) {
      console.error("Error creating person data: ", error.response.data);
      throw new Error(error.response.data.message || "Unknown server error");
    } else {
      console.error("Error creating person data: ", error);
      throw new Error(error.message || "Unknown error");
    }
  }
};

export const deletePersonData = async (id) => {
  try {
    const response = await axios.delete(
      `http://127.0.0.1:8000/hospital/person/${id}`
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

export const updatePersonData = async (id, updatedPersonData) => {
  try {
    const response = await axios.put(
      `http://127.0.0.1:8000/hospital/person/${id}`,
      updatedPersonData
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
