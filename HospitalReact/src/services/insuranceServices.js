import {addInsurance} from "../api/insurance.js";
import {toast} from "react-hot-toast";
import {format, parseISO} from "date-fns";

export const addInsuranceData = async (idUser, company, number, status, term) => {
    if (!idUser || !company || !number || !status || !term) {
        toast.error("Please fill in all fields");
        return;
    }
    try {
        const formattedDateTerm = format(parseISO(term), "dd/MM/yyyy");

        const formData = {
            idUser, company, number, status, term: formattedDateTerm
        };
        console.log("Datos enviados en la solicitud POST:", formData);
        const response = await addInsurance(formData);
        toast.success("Insurance created successfully");
    } catch (error) {
        if (error instanceof Error) {
            toast.error(error.message);
        } else {
            toast.error("Unknown error occurred");
        }
        console.error("Error creating person: ", error);
    }
};