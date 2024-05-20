/* eslint-disable no-unused-vars */
import React, { useState, useEffect } from "react";
import { BiChevronDown, BiPlus } from "react-icons/bi";
import Layout from "../Layout";
import { Select } from "../components/Form";
import { MedicineTable } from "../components/Tables";
import { sortsDatas } from "../components/Datas";
import AddEditMedicineModal from "../components/Modals/Medicine/AddEditMedicine";
import DeleteMedicationModal from "../components/Modals/Medicine/DeleteMedicationModal";
import { loadMedications } from "../services/medicationServices";

function Medicine() {
  const [isOpen, setIsOpen] = useState(false);
  const [isOpenDeleteModal, setIsOpenDeleteModal] = useState(false);
  const [data, setData] = useState([]);
  const [currentMedicine, setCurrentMedicine] = useState(null);
  const [status, setStatus] = useState(sortsDatas.stocks[0]);
  const [error, setError] = useState(null);

  const loadData = async () => {
    await loadMedications(setData, setError);
  };

  useEffect(() => {
    loadData();
  }, []);

  const onCloseModal = () => {
    setIsOpen(false);
    setCurrentMedicine(null);
  };

  const onCloseDeleteModal = () => {
    setIsOpenDeleteModal(false);
    setCurrentMedicine(null);
  };

  const onDelete = (datas) => {
    setCurrentMedicine(datas);
    setIsOpenDeleteModal(true);
  };

  const onEdit = (datas) => {
    setIsOpen(true);
    setCurrentMedicine(datas);
  };

  return (
    <Layout>
      {isOpen && (
        <AddEditMedicineModal
          isOpen={isOpen}
          datas={currentMedicine}
          closeModal={onCloseModal}
          onMedicationAdded={loadData}
        />
      )}
      {isOpenDeleteModal && (
        <DeleteMedicationModal
          isOpen={isOpenDeleteModal}
          datas={currentMedicine}
          closeModal={onCloseDeleteModal}
          onMedicationDelete={loadData}
        />
      )}
      {/* add button */}
      <button
        onClick={() => setIsOpen(true)}
        className="w-16 animate-bounce h-16 border border-border z-50 bg-subMain text-white rounded-full flex-colo fixed bottom-8 right-12 button-fb"
      >
        <BiPlus className="text-2xl" />
      </button>
      {/*  */}
      <h1 className="text-xl font-semibold">Medicine</h1>
      <div
        data-aos="fade-up"
        data-aos-duration="1000"
        data-aos-delay="100"
        data-aos-offset="200"
        className="bg-white my-8 rounded-xl border-[1px] border-border p-5"
      >
        {/* datas */}
        <div className="grid md:grid-cols-6 grid-cols-1 gap-2">
          <div className="md:col-span-5 grid lg:grid-cols-4 xs:grid-cols-2 items-center gap-2">
            <input
              type="text"
              placeholder='Search "paracetamol"'
              className="h-14 w-full text-sm text-main rounded-md bg-dry border border-border px-4"
            />
            <Select
              selectedPerson={status}
              setSelectedPerson={setStatus}
              datas={sortsDatas.stocks}
            >
              <div className="w-full flex-btn text-main text-sm p-4 border bg-dry border-border font-light rounded-lg focus:border focus:border-subMain">
                {status.name} <BiChevronDown className="text-xl" />
              </div>
            </Select>
          </div>
        </div>
        <div className="mt-8 w-full overflow-x-scroll">
          <MedicineTable data={data} onEdit={onEdit} onDelete={onDelete}/>
        </div>
      </div>
    </Layout>
  );
}

export default Medicine;
