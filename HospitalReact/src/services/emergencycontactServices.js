import {addEmergencyContact} from "../api/emergencycontact.js";
import {toast} from "react-hot-toast";

export const addEmergencyContactData = async (idUser, name, relationship, phoneNumber) => {
    if (!idUser || !name || !relationship || !phoneNumber) {
        toast.error("Please fill in all fields");
        return;
    }
    try {
        const formData = {
            idUser, name, relationship, phoneNumber
        };
        console.log("Datos enviados en la solicitud POST:", formData);
        const response = await addEmergencyContact(formData);
        toast.success("Contact created successfully");
    } catch (error) {
        if (error instanceof Error) {
            toast.error(error.message);
        } else {
            toast.error("Unknown error occurred");
        }
        console.error("Error creating person: ", error);
    }
};