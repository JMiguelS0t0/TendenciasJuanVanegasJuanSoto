/* eslint-disable no-unused-vars */
import React, { useState, useEffect } from "react";
import { MdOutlineCloudDownload } from "react-icons/md";
import { toast } from "react-hot-toast";
import { BiPlus } from "react-icons/bi";
import Layout from "../../Layout";
import { Button } from "../../components/Form";
import { PersonsTable } from "../../components/Tables";
import AddPersonModal from "../../components/Modals/Person/AddPersonModal";
import { loadpersonsData } from "../../services/personServices";

function Doctors() {
  const [isOpen, setIsOpen] = useState(false);
  const [personsData, setPersonData] = useState([]);
  const [error, setError] = useState(null);
  const [editingPerson, setEditingPerson] = useState(null);

  const loadData = async () => {
    await loadpersonsData(setPersonData, setError);
  };

  useEffect(() => {
    loadData();
  }, []);

  const onCloseModal = () => {
    setIsOpen(false);
    setEditingPerson(null);
  };

  const preview = async (data) => {
    setEditingPerson(data);
    setIsOpen(true);
  };

  const handleDelete = async () => {
    await loadData();
  };

  return (
    <Layout>
      {
        // Modal para agregar doctor
        isOpen && (
          <AddPersonModal
            closeModal={onCloseModal}
            isOpen={isOpen}
            doctor={true}
            datas={editingPerson}
            onPersonAdded={loadData}
          />
        )
      }
      {/* Botón para agregar doctor */}
      <button
        onClick={() => setIsOpen(true)}
        className="w-16 animate-bounce h-16 border border-border z-50 bg-subMain text-white rounded-full flex-colo fixed bottom-8 right-12 button-fb"
      >
        <BiPlus className="text-2xl" />
      </button>
      {/* Encabezado */}
      <h1 className="text-xl font-semibold">Persons</h1>
      <div
        data-aos="fade-up"
        data-aos-duration="1000"
        data-aos-delay="100"
        data-aos-offset="200"
        className="bg-white my-8 rounded-xl border-[1px] border-border p-5"
      >
        {/* Filtros y botón de exportación */}
        <div className="grid md:grid-cols-6 sm:grid-cols-2 grid-cols-1 gap-2">
          <div className="md:col-span-5 grid lg:grid-cols-4 items-center gap-6">
            <input
              type="text"
              placeholder='Search "daudi mburuge"'
              className="h-14 w-full text-sm text-main rounded-md bg-dry border border-border px-4"
            />
          </div>
          <Button
            label="Export"
            Icon={MdOutlineCloudDownload}
            onClick={() => {
              toast.error("Exporting is not available yet");
            }}
          />
        </div>
        {/* Tabla de doctores */}
        <div className="mt-8 w-full overflow-x-scroll">
          <PersonsTable
            doctor={true}
            data={personsData}
            functions={{
              preview: preview,
            }}
            onDelete={handleDelete}
          />
        </div>
      </div>
    </Layout>
  );
}

export default Doctors;
