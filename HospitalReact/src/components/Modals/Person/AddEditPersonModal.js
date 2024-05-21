import React, { useState, useEffect } from "react";
import Modal from "../Modal";
import { Button, Input, Select } from "../../Form";
import { BiChevronDown } from "react-icons/bi";
import { HiOutlineCheckCircle } from "react-icons/hi";
import { sortsDatas } from "../../Datas";
import { addPerson, updatePerson } from "../../../services/personServices";

const useField = (initialValue = "") => {
  const [value, setValue] = useState(initialValue);

  const onChange = (event) => {
    setValue(event.target.value);
  };

  return { value, onChange };
};

function AddEditPersonModal({ closeModal, isOpen, doctor, datas, onPersonAdded }) {
  const [instraction, setInstraction] = useState(sortsDatas.roles[0]);
  const [isEditing, setIsEditing] = useState(false);

  const name = useField(datas ? datas.name : "");
  const cedula = useField(datas ? datas.cedula : "");
  const email = useField(datas ? datas.email : "");
  const phoneNumber = useField(datas ? datas.phoneNumber : "");
  const dateBirth = useField(datas ? datas.dateBirth : "");
  const address = useField(datas ? datas.address : "");
  const userName = useField(datas ? datas.userName : "");
  const password = useField(datas ? datas.password : "");
  console.log(datas);

  useEffect(() => {
    setIsEditing(!!datas);
  }, [datas]);

  const handleSubmit = async () => {
    if (isEditing) {
      console.log("Editando");
      await updatePerson(
        name.value,
        cedula.value,
        email.value,
        phoneNumber.value,
        dateBirth.value,
        address.value,
        userName.value,
        password.value,
        instraction,
        closeModal
      );
    } else {
      await addPerson(
        name.value,
        cedula.value,
        email.value,
        phoneNumber.value,
        dateBirth.value,
        address.value,
        userName.value,
        password.value,
        instraction,
        closeModal
      );
    }
    onPersonAdded();
  };

  return (
    <Modal
      closeModal={closeModal}
      isOpen={isOpen}
      title={doctor ? (isEditing ? "Edit Person" : "Add Person") : "Add Person"}
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
            placeholder="DD/MM/YYYY"
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

export default AddEditPersonModal;
