import {Button, Input, Select} from "./Form.jsx";
import {RiDeleteBin5Line} from "react-icons/ri";
import {toast} from "react-hot-toast";
import useField from "../hooks/useField.js";
import {addPatient} from "../services/patientServices.js";
import {addEmergencyContactData} from "../services/emergencycontactServices.js";
import {addInsuranceData} from "../services/insuranceServices.js";
import {HiOutlineCheckCircle} from "react-icons/hi";
import {useNavigate} from "react-router-dom";
import {useState} from "react";
import {sortsDatas} from "./Datas.jsx";
import {BiChevronDown} from "react-icons/bi";


function InsuranceForm({patientData, emergencyContactInfo, onCancel}) {
    const company = useField("");
    const number = useField("");
    const term = useField("");
    const [status, setStatus] = useState(sortsDatas.statusInsurance[0])
    const navigate = useNavigate()

    const handleSubmit = async () => {
        if (!company.value || !number.value || !status.name || !term.value) {
            toast.error("Please fill in all fields (Insurance)");
            return;
        }

        try {
            // Send patient data to the server
            await addPatient(
                patientData.idNumber,
                patientData.name,
                patientData.dateBirth,
                patientData.gender,
                patientData.address,
                patientData.phoneNumber,
                patientData.email
            );

            // Send emergency contact data to the server
            await addEmergencyContactData(
                emergencyContactInfo.idUser,
                emergencyContactInfo.name,
                emergencyContactInfo.relationship,
                emergencyContactInfo.phoneNumber
            );

            // Send insurance data to the server
            await addInsuranceData(
                emergencyContactInfo.idUser,
                company.value,
                number.value,
                status.name,
                term.value
            );

            toast.success("All data submitted successfully!");
            navigate("/patients");
        } catch (error) {
            console.error("Failed to submit data:", error);
            toast.error("Failed to submit data.");
        }
    };

    return (
        <div className="flex-colo gap-4">
            <Input
                label="Insurance Company"
                color={true}
                type="text"
                name="company"
                register={company}
                placeholder="Enter insurance company"
            />
            <Input
                label="Insurance Number"
                color={true}
                type="text"
                name="number"
                register={number}
                placeholder="Enter insurance number"
            />
            <div className="flex w-full flex-col gap-3">
                <p className="text-black text-sm">status</p>
                <Select
                    selectedPerson={status}
                    setSelectedPerson={setStatus}
                    datas={sortsDatas.statusInsurance}
                >
                    <div
                        className="w-full flex-btn text-textGray text-sm p-4 border border-border font-light rounded-lg focus:border focus:border-subMain">
                        {status?.name} <BiChevronDown className="text-xl"/>
                    </div>
                </Select>
            </div>
            <Input
                label="Insurance Term"
                color={true}
                type="date"
                name="term"
                register={term}
                placeholder="Enter insurance term"
            />
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 w-full">
                <Button
                    label="Cancel"
                    Icon={RiDeleteBin5Line}
                    onClick={onCancel}
                />
                <Button
                    label="Submit"
                    Icon={HiOutlineCheckCircle}
                    onClick={handleSubmit}
                />
            </div>
        </div>
    );
}

export default InsuranceForm;
