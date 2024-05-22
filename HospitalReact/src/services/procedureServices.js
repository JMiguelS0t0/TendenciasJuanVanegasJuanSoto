import { toast } from "react-hot-toast";

import {
  getProcedures,
  addProcedure,
  deleteProcedure,
  updateProcedure,
} from "../api/procedure.js";

export const loadProcedures = async (setProcedureData, setError) => {
  try {
    const data = await getProcedures();
    setProcedureData(data);
  } catch (error) {
    setError(error);
    toast.error(error.response.data.message);
  }
};

export const deleteProcedureData = async (id) => {
  console.log("Id to delete: ", id);
  try {
    await deleteProcedure(id);
    toast.success("Procedure deleted successfully");
  } catch (error) {
    toast.error(`Error deleting procedure: ${error.message}`);
  }
};

export const createProcedure = async (name, cost, closeModal) => {
  if (!name || !cost) {
    toast.error("Please fill in all fields");
    return;
  }
  try {
    const formData = {
      name: name,
      cost,
    };
    console.log("Data sent in POST: ", formData);
    await addProcedure(formData);
    toast.success("Procedure added successfully");
    closeModal();
  } catch (error) {
    if (error instanceof Error) {
      toast.error(error.message);
    } else {
      toast.error("Unknown error occurred");
    }
    console.error("Error creating procedure: ", error);
  }
};

export const updateProcedureData = async (id, name, cost, closeModal) => {
  if (!name || !cost) {
    toast.error("Please fill in all fields");
    return;
  }
  try {
    const formData = {
      name: name,
      cost,
    };
    console.log("Data sent in PUT: ", formData);
    await updateProcedure(id, formData);
    toast.success("Procedure updated successfully");
    closeModal();
  } catch (error) {
    if (error instanceof Error) {
      toast.error(error.message);
    } else {
      toast.error("Unknown error occurred");
    }
    console.error("Error updating procedure: ", error);
  }
};
