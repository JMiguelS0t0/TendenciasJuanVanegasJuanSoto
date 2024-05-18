import React, { useState } from "react";
import Modal from "./Modal";
import { Button, Input, Select } from "../Form";
import { BiChevronDown } from "react-icons/bi";
import { HiOutlineCheckCircle } from "react-icons/hi";
import { toast } from "react-hot-toast";
import { sortsDatas } from "../Datas";
import { createPersonData } from "../Datas";

const useField = () => {
  const [value, setValue] = useState("");

  const onChange = (event) => {
    setValue(event.target.value);
  };

  return { value, onChange };
};

function AddPersonModal({ closeModal, isOpen, doctor, datas }) {
  const [instraction, setInstraction] = useState(sortsDatas.roles[0]);

  const name = useField();
  const cedula = useField();
  const email = useField();
  const phoneNumber = useField();
  const dateBirth = useField();
  const address = useField();
  const userName = useField();
  const password = useField();

  const handleSubmit = async () => {
    try {
      const formData = {
        name: name.value,
        cedula: cedula.value,
        email: email.value,
        phoneNumber: phoneNumber.value,
        dateBirth: dateBirth.value,
        address: address.value,
        userName: userName.value,
        password: password.value,
        rol: instraction.name,
      };
  
      console.log("Datos enviados en la solicitud POST:", formData);
      await createPersonData(formData);
      toast.success("Person created successfully");
      closeModal();
    } catch (error) {
      if (
        error.response &&
        error.response.data &&
        error.response.data.message
      ) {
        toast.error(error.response.data.message);
      } else {
        toast.error("Error creating person: " + JSON.stringify(error));
      }
      console.error("Error creating person: ", error);
      throw error; 
    }
  };
  

  return (
    <Modal
      closeModal={closeModal}
      isOpen={isOpen}
      title={doctor ? "Add Person" : datas?.id ? "Edit Person" : "Add Person"}
      width={"max-w-3xl"}
    >
      <div className="flex-colo gap-6">
        <Input
          label="Cedula"
          color={true}
          placeholder="1040570758"
          name="cedula"
          register={cedula}
        />

        <div className="grid sm:grid-cols-2 gap-4 w-full">
          <Input
            label="Full Name"
            color={true}
            placeholder="John Doe"
            name="name"
            register={name}
          />

          <div className="flex w-full flex-col gap-3">
            <p className="text-black text-sm">Rol</p>
            <Select
              selectedPerson={instraction}
              setSelectedPerson={setInstraction}
              datas={sortsDatas.roles}
            >
              <div className="w-full flex-btn text-textGray text-sm p-4 border border-border font-light rounded-lg focus:border focus:border-subMain">
                {instraction.name} <BiChevronDown className="text-xl" />
              </div>
            </Select>
          </div>
        </div>

        <div className="grid sm:grid-cols-2 gap-4 w-full">
          <Input
            label="Email"
            color={true}
            name="email"
            placeholder="example@example.com"
            register={email}
          />
          <Input
            label="Phone Number"
            color={true}
            name="phoneNumber"
            register={phoneNumber}
          />
        </div>

        <div className="grid sm:grid-cols-2 gap-4 w-full">
          <Input
            label="Date birth"
            color={true}
            name="dateBirth"
            placeholder="12/12/1995"
            register={dateBirth}
          />
          <Input
            label="Address"
            color={true}
            name="address"
            register={address}
          />
        </div>

        {/* userName */}
        <Input
          label="Username"
          color={true}
          name="userName"
          register={userName}
        />

        {/* password */}
        <Input
          label="Password"
          color={true}
          name="password"
          register={password}
        />

        {/* buttones */}
        <div className="grid sm:grid-cols-2 gap-4 w-full">
          <button
            onClick={closeModal}
            className="bg-red-600 bg-opacity-5 text-red-600 text-sm p-4 rounded-lg font-light"
          >
            Cancel
          </button>
          <Button
            label="Save"
            Icon={HiOutlineCheckCircle}
            onClick={handleSubmit}
          />
        </div>
      </div>
    </Modal>
  );
}

export default AddPersonModal;
