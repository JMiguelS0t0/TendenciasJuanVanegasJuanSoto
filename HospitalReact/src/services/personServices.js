import {
  fetchPersonData,
  deletePersonData,
  createPersonData,
  updatePersonData,
} from "../api/person";
import { toast } from "react-hot-toast";

export const loadpersonsData = async (setPersonData, setError, id = null) => {
  try {
    const data = await fetchPersonData(id);
    setPersonData(data);
  } catch (error) {
    setError(error);
    toast.error(error.response.data.message);
  }
};

export const handleDelete = async (id) => {
  console.log("ID to delete:", id);
  try {
    await deletePersonData(id);
    toast.success("Transaction deleted successfully");
  } catch (error) {
    toast.error(`Error deleting transaction: ${error.message}`);
  }
};

export const addPerson = async (
  name,
  cedula,
  email,
  phoneNumber,
  dateBirth,
  address,
  userName,
  password,
  instraction,
  closeModal
) => {
  if (
    !name ||
    !cedula ||
    !email ||
    !phoneNumber ||
    !dateBirth ||
    !address ||
    !userName ||
    !password
  ) {
    toast.error("Please fill in all fields");
    return;
  }

  try {
    const formData = {
      name,
      cedula,
      email,
      phoneNumber,
      dateBirth,
      address,
      userName,
      password,
      rol: instraction.name,
    };

    console.log("Datos enviados en la solicitud POST:", formData);
    await createPersonData(formData);
    toast.success("Person created successfully");
    closeModal();
  } catch (error) {
    if (error instanceof Error) {
      toast.error(error.message);
    } else {
      toast.error("Unknown error occurred");
    }
    console.error("Error creating person: ", error);
  }
};

export const updatePerson = async (
  name,
  cedula,
  email,
  phoneNumber,
  dateBirth,
  address,
  userName,
  password,
  instraction,
  closeModal
) => {
  if (
    !name ||
    !cedula ||
    !email ||
    !phoneNumber ||
    !dateBirth ||
    !address ||
    !userName ||
    !password
  ) {
    toast.error("Please fill in all fields");
    return;
  }
  try {
    const updatedPersonData = {
      name,
      cedula,
      email,
      phoneNumber,
      dateBirth,
      address,
      userName,
      password,
      rol: instraction.name,
    };

    console.log("Datos enviados en la solicitud PUT:", updatedPersonData);
    await updatePersonData(cedula, updatedPersonData);
    toast.success("Person updated successfully");
    closeModal();
  } catch (error) {
    if (error instanceof Error) {
      toast.error(error.message);
    } else {
      toast.error("Unknown error occurred");
    }
    console.error("Error updating person: ", error);
  }
};
