import {fetchPatientData, createPatientData, deletePatientData} from "../api/patient.js";
import {toast} from "react-hot-toast";
import {format, parseISO} from "date-fns";

export const loadPatientData = async (setPatientData, setError, id = null) => {
    try {
        const data = await fetchPatientData(id);
        setPatientData(data);
    } catch (error) {
        setError(error);
        toast.error(error.response.data.message);
    }
};

export const addPatient = async (idNumber, name, dateBirth, gender, address, phoneNumber, email) => {
    if (!idNumber || !name || !dateBirth || !gender || !address || !phoneNumber || !email) {
        toast.error("Please fill in all fields");
        return;
    }
    try {
        const formattedDateBirth = format(parseISO(dateBirth), "dd/MM/yyyy");

        const formData = {
            idNumber, name, dateBirth: formattedDateBirth, gender, address, phoneNumber, email
        };

        console.log("Datos enviados en la solicitud POST:", formData);
        const response = await createPatientData(formData);
        toast.success("Person created successfully");
    } catch (error) {
        if (error instanceof Error) {
            toast.error(error.message);
        } else {
            toast.error("Unknown error occurred");
        }
        console.error("Error creating person: ", error);
    }
};

export const handleDelete = async (id) => {
    console.log("ID to delete:", id);
    try {
        await deletePatientData(id);
        toast.success("Transaction deleted successfully");
    } catch (error) {
        toast.error(`Error deleting transaction: ${error.message}`);
    }
};