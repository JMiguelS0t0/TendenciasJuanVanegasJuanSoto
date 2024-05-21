/* eslint-disable no-unused-vars */
import React, { useState, useEffect } from "react";
import { BiPlus } from "react-icons/bi";
import Layout from "../Layout";
import { MedicineTable } from "../components/Tables";
import AddEditMedicineModal from "../components/Modals/Medicine/AddEditMedicine";
import DeleteMedicationModal from "../components/Modals/Medicine/DeleteMedicationModal";
import { loadMedications } from "../services/medicationServices";

function Medicine() {
  const [isOpen, setIsOpen] = useState(false);
  const [isOpenDeleteModal, setIsOpenDeleteModal] = useState(false);
  const [data, setData] = useState([]);
  const [currentMedicine, setCurrentMedicine] = useState(null);
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
      {/* ADD/EDIT MODAL */}
      {isOpen && (
        <AddEditMedicineModal
          isOpen={isOpen}
          datas={currentMedicine}
          closeModal={onCloseModal}
          onMedicationAdded={loadData}
        />
      )}
      {/* DELETE MODAL */}
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
        <div className="mt-8 w-full overflow-x-scroll">
          <MedicineTable data={data} onEdit={onEdit} onDelete={onDelete} />
        </div>
      </div>
    </Layout>
  );
}

export default Medicine;
