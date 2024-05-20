/* eslint-disable no-unused-vars */
import React, { useState, useEffect } from "react";
import { BiPlus } from "react-icons/bi";
import Layout from "../../Layout";
import { PersonsTable } from "../../components/Tables";
import AddPersonModal from "../../components/Modals/Person/AddPersonModal";
import DeletePersonModal from "../../components/Modals/Person/DeletePersonModal";
import { loadpersonsData } from "../../services/personServices";
import { Button } from "../../components/Form";

function Doctors() {
  const [isOpen, setIsOpen] = useState(false);
  const [personsData, setPersonData] = useState([]);
  const [searchCedula, setSearchCedula] = useState("");
  const [error, setError] = useState(null);

  const [selectedPerson, setSelectedPerson] = useState({
    editing: null,
    deleting: null,
  });
  const [isDeleteModalOpen, setDeleteModal] = useState(false);

  const loadData = async () => {
    await loadpersonsData(setPersonData, setError, searchCedula);
  };

  useEffect(() => {
    if (searchCedula === "") {
      loadData();
    }
  }, [searchCedula]);

  const onCloseModal = () => {
    setIsOpen(false);
    setSelectedPerson({ ...selectedPerson, editing: null });
  };

  const preview = async (data) => {
    setSelectedPerson({ ...selectedPerson, editing: data });
    setIsOpen(true);
  };

  const onCloseDeleteModal = () => {
    setDeleteModal(false);
    setSelectedPerson({ ...selectedPerson, deleting: null });
  };

  const handleDelete = async (cedula) => {
    const person = personsData.find((p) => p.cedula === cedula);
    console.log(person);
    if (person) {
      setSelectedPerson({ ...selectedPerson, deleting: person.cedula });
      setDeleteModal(true);
    }
  };

  return (
    <Layout>
      {
        // Modal para agregar empleado
        isOpen && (
          <AddPersonModal
            closeModal={onCloseModal}
            isOpen={isOpen}
            doctor={true}
            datas={selectedPerson.editing}
            onPersonAdded={loadData}
          />
        )
      }
      {
        // Modal para borrar empleado
        isDeleteModalOpen && (
          <DeletePersonModal
            closeModal={onCloseDeleteModal}
            isOpen={isDeleteModalOpen}
            datas={selectedPerson.deleting}
            onPersonDelete={loadData}
          />
        )
      }
      {/* Botón para agregar empleado */}
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
        {/* Filtros*/}
        <div className="grid md:grid-cols-6 sm:grid-cols-2 grid-cols-1 gap-2">
          <div className="md:col-span-5 grid lg:grid-cols-2 items-center gap-6">
            <input
              type="number"
              placeholder="Search by Cedula"
              value={searchCedula}
              onChange={(e) => setSearchCedula(e.target.value)}
              className="h-14 w-full text-sm text-main rounded-md bg-dry border border-border px-4"
            />
          </div>
          <Button label="Buscar" onClick={loadData} />
        </div>
        {/* Tabla de empleados */}
        <div className="mt-8 w-full overflow-x-scroll">
          <PersonsTable
            doctor={true}
            data={personsData}
            functions={{
              preview: preview,
              onDelete: handleDelete,
            }}
          />
        </div>
      </div>
    </Layout>
  );
}

export default Doctors;
