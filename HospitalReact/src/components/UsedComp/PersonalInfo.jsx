import {useState} from "react";
import {Button, Input, Select} from "../Form";
import {BiChevronDown} from "react-icons/bi";
import {HiOutlineCheckCircle} from "react-icons/hi";
import {RiDeleteBin5Line} from "react-icons/ri";
import {toast} from "react-hot-toast";
import {sortsDatas} from "../Datas";
import useField from "../../hooks/useField";
import EmergencyContactForm from "../EmergencyContactForm";
import {useNavigate} from "react-router-dom";

function PersonalInfo() {
    const [gender, setGender] = useState(sortsDatas.genderFilter[0]);
    const [showEmergencyForm, setShowEmergencyForm] = useState(false);
    const [patientData, setPatientData] = useState(null);
    const navigate = useNavigate();

    const idNumber = useField("");
    const name = useField("");
    const address = useField("");
    const phoneNumber = useField("");
    const email = useField("");
    const dateBirth = useField("");

    const handleNext = () => {
        if (!idNumber.value || !name.value || !dateBirth.value || !gender.name || !address.value || !phoneNumber.value || !email.value) {
            toast.error("Please fill in all fields (Patient)");
            return;
        }

        const patientInfo = {
            idNumber: idNumber.value,
            name: name.value,
            dateBirth: dateBirth.value,
            gender: gender.name,
            address: address.value,
            phoneNumber: phoneNumber.value,
            email: email.value,
        };

        console.log("Patient Info:", patientInfo);
        setPatientData(patientInfo);
        setShowEmergencyForm(true);
    };

    const handleCancel = () => {
        navigate("/patients");
    };

    if (showEmergencyForm) {
        return (
            <EmergencyContactForm
                patientData={patientData}
                onCancel={handleCancel}
            />
        );
    }

    return (
        <div className="flex flex-col gap-4">
            <div className="flex gap-4">
                <Input
                    label="Id"
                    color={true}
                    type="text"
                    name="idNumber"
                    register={idNumber}
                    placeholder="Enter ID number"
                />
                <Input
                    label="Full Name"
                    color={true}
                    type="text"
                    name="name"
                    register={name}
                    placeholder="Enter full name"
                />
            </div>
            <div className="flex gap-4">
                <Input
                    label="Date of Birth"
                    color={true}
                    type="date"
                    name="dateBirth"
                    register={dateBirth}
                    placeholder="DD/MM/YYYY"
                />
                <div className="flex w-full flex-col gap-3">
                    <p className="text-black text-sm">Gender</p>
                    <Select
                        selectedPerson={gender}
                        setSelectedPerson={setGender}
                        datas={sortsDatas.genderFilter}
                    >
                        <div
                            className="w-full flex-btn text-textGray text-sm p-4 border border-border font-light rounded-lg focus:border focus:border-subMain">
                            {gender?.name} <BiChevronDown className="text-xl"/>
                        </div>
                    </Select>
                </div>
            </div>
            <div className="flex gap-4">
                <Input
                    label="Address"
                    color={true}
                    type="text"
                    name="address"
                    register={address}
                    placeholder="Enter address"
                />
                <Input
                    label="Phone Number"
                    color={true}
                    type="number"
                    name="phoneNumber"
                    register={phoneNumber}
                    placeholder="Enter phone number"
                />
            </div>
            <Input
                label="Email"
                color={true}
                type="email"
                name="email"
                register={email}
                placeholder="Enter email"
            />
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <Button
                    label="Cancel"
                    Icon={RiDeleteBin5Line}
                    onClick={() => {
                        handleCancel();
                    }}
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

export default PersonalInfo;
