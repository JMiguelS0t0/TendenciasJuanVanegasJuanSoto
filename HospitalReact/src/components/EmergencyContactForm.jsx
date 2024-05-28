import {Button, Input} from "./Form.jsx";
import {RiDeleteBin5Line} from "react-icons/ri";
import {toast} from "react-hot-toast";
import useField from "../hooks/useField.js";
import InsuranceForm from "./InsuranceForm";
import {HiOutlineCheckCircle} from "react-icons/hi";
import {useState} from "react";

function EmergencyContactForm({patientData, onCancel}) {
    const [showInsuranceForm, setShowInsuranceForm] = useState(false);
    const contactName = useField("");
    const relationship = useField("");
    const contactPhoneNumber = useField("");

    const handleNext = () => {
        if (!contactName.value || !relationship.value || !contactPhoneNumber.value) {
            toast.error("Please fill in all fields (Emergency Contact)");
            return;
        }

        const emergencyContactInfo = {
            idUser: patientData.idNumber,
            contactName: contactName.value,
            relationship: relationship.value,
            contactPhoneNumber: contactPhoneNumber.value,
        };

        console.log("Emergency Contact Info:", emergencyContactInfo);
        setShowInsuranceForm(true);
    };

    if (showInsuranceForm) {
        return (
            <InsuranceForm
                patientData={patientData}
                emergencyContactInfo={{
                    idUser: patientData.idNumber,
                    name: contactName.value,
                    relationship: relationship.value,
                    phoneNumber: contactPhoneNumber.value,
                }}
                onCancel={onCancel}
            />
        );
    }

    return (
        <div className="flex-colo gap-4">
            <Input
                label="Contact Name"
                color={true}
                type="text"
                name="contactName"
                register={contactName}
                placeholder="Enter contact name"
            />
            <Input
                label="Relationship"
                color={true}
                type="text"
                name="relationship"
                register={relationship}
                placeholder="Enter relationship"
            />
            <Input
                label="Contact Phone Number"
                color={true}
                type="number"
                name="contactPhoneNumber"
                register={contactPhoneNumber}
                placeholder="Enter contact phone number"
            />
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 w-full">
                <Button
                    label="Cancel"
                    Icon={RiDeleteBin5Line}
                    onClick={onCancel}
                />
                <Button
                    label="Next"
                    Icon={HiOutlineCheckCircle}
                    onClick={handleNext}
                />
            </div>
        </div>
    );
}

export default EmergencyContactForm;
