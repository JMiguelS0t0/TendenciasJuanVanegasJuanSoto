import {
  getMedications,
  addMedication,
  updateMedicationData,
  deleteMedicine,
} from "../api/medicine";
import { toast } from "react-hot-toast";

export const loadMedications = async (setMedicationData, setError) => {
  try {
    const data = await getMedications();
    setMedicationData(data);
  } catch (error) {
    setError(error);
    toast.error(error.response.data.message);
  }
};

export const deleteMedication = async (id) => {
  console.log("Id to delete: ", id);
  try {
    await deleteMedicine(id);
    toast.success("Medication deleted successfully");
  } catch (error) {
    toast.error(`Error deleting transaction: ${error.message}`);
  }
};

export const createMedication = async (name, cost, closeModal) => {
  if (!name || !cost) {
    toast.error("Please fill in all fields");
    return;
  }
  try {
    const formData = {
      name: name,
      cost,
    };
    console.log("Datos enviados en el POST: ", formData);
    await addMedication(formData);
    toast.success("Medication added successfully");
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

export const updateMedication = async (id, name, cost, closeModal) => {
  if (!name || !cost) {
    toast.error("Please fill in all fields");
    return;
  }
  try {
    const formData = {
      name: name,
      cost,
    };
    console.log("Dato del PUT: ", formData);
    await updateMedicationData(id, formData);
    toast.success("Medication updated successfully");
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
