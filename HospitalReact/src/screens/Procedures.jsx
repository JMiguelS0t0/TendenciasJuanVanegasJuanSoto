import { useState, useEffect } from "react";
import { BiPlus } from "react-icons/bi";
import Layout from "../Layout/index.jsx";
import { ProcedureTable } from "../components/Tables";
import AddEditProcedureModal from "../components/Modals/Procedure/AddEditProcedureModal";
import DeleteProcedureModal from "../components/Modals/Procedure/DeleteProcedureModal";
import { loadProcedures } from "../services/procedureServices.js";

function Procedures() {
  const [isOpen, setIsOpen] = useState(false);
  const [isOpenDeleteModal, setIsOpenDeleteModal] = useState(false);
  const [data, setData] = useState([]);
  const [currentProcedure, setCurrentProcedure] = useState(null);
  // eslint-disable-next-line no-unused-vars
  const [error, setError] = useState(null);

  const loadData = async () => {
    await loadProcedures(setData, setError);
  };

  useEffect(() => {
    loadData();
  }, []);

  const onCloseModal = () => {
    setIsOpen(false);
    setCurrentProcedure(null);
  };

  const onCloseDeleteModal = () => {
    setIsOpenDeleteModal(false);
    setCurrentProcedure(null);
  };

  const onDelete = (datas) => {
    setCurrentProcedure(datas);
    setIsOpenDeleteModal(true);
  };

  const onEdit = (datas) => {
    setIsOpen(true);
    setCurrentProcedure(datas);
  };

  return (
    <Layout>
      {/* ADD MODAL */}
      {isOpen && (
        <AddEditProcedureModal
          isOpen={isOpen}
          datas={currentProcedure}
          closeModal={onCloseModal}
          onProcedureAdded={loadData}
        />
      )}
      {/* DELETE MODAL */}
      {isOpenDeleteModal && (
        <DeleteProcedureModal
          isOpen={isOpenDeleteModal}
          datas={currentProcedure}
          closeModal={onCloseDeleteModal}
          onProcedureDelete={loadData}
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
      <h1 className="text-xl font-semibold">Procedures</h1>
      <div
        data-aos="fade-up"
        data-aos-duration="1000"
        data-aos-delay="100"
        data-aos-offset="200"
        className="bg-white my-8 rounded-xl border-[1px] border-border p-5"
      >
        <div className="mt-8 w-full overflow-x-scroll">
          <ProcedureTable data={data} onEdit={onEdit} onDelete={onDelete} />
        </div>
      </div>
    </Layout>
  );
}

export default Procedures;
