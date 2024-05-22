import {
    getDiagnosticaids,
    addDiagnosticaid,
    updateDiagnosticaid,
    deleteDiagnosticaid,
} from "../api/diagnosticaid.js";
import { toast } from "react-hot-toast";

export const loadDiagnostic = async (setDiagnosticData, setError) => {
    try {
        const data = await getDiagnosticaids();
        setDiagnosticData(data);
    } catch (error) {
        setError(error);
        toast.error(error.response.data.message);
    }
};

export const deleteDiagnostic = async (id) => {
    console.log("Id to delete: ", id);
    try {
        await deleteDiagnosticaid(id);
        toast.success("Diagnostic Aid deleted successfully");
    } catch (error) {
        toast.error(`Error deleting transaction: ${error.message}`);
    }
};

export const createDiagnostic = async (name, cost, closeModal) => {
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
        await addDiagnosticaid(formData);
        toast.success("Diagnostic Aid added successfully");
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

export const updateDiagnostic = async (id, name, cost, closeModal) => {
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
        await updateDiagnosticaid(id, formData);
        toast.success("Diagnostic Aid updated successfully");
        closeModal();
    } catch (error) {
        if (error instanceof Error) {
            toast.error(error.message);
        } else {
            toast.error("Unknown error occurred");
        }
        console.error("Error updating diagnostic Aid: ", error);
    }
};
