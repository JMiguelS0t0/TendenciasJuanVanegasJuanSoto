import Modal from "../Modal";
import { Button } from "../../Form";
import { HiOutlineCheckCircle } from "react-icons/hi";
import { toast } from "react-hot-toast";

import { handleDelete } from "../../../services/personServices";

function DeletePersonModal({ closeModal, isOpen, datas, onPersonDelete }) {
  const handleSubmit = async () => {
    try {
      await handleDelete(datas);
    } catch (error) {
      console.log("Error: ", error);
      toast.error("Error al eliminar la persona");
    }
    closeModal();
    onPersonDelete();
  };

  return (
    <Modal
      closeModal={closeModal}
      isOpen={isOpen}
      title={"Delete Person"}
      width={"max-w-3xl"}
    >
      <div className="flex-colo gap-6">
        <p>
          ¿Estás seguro que deseas eliminar al usuario con cédula:{" "}
          <span class="font-medium">{datas}</span> ?
        </p>
        {/* buttones */}
        <div className="grid sm:grid-cols-2 gap-4 w-full">
          <button
            onClick={closeModal}
            className="bg-red-600 bg-opacity-5 text-red-600 text-sm p-4 rounded-lg font-light"
          >
            Cancel
          </button>
          <Button
            label="Confirmar"
            Icon={HiOutlineCheckCircle}
            onClick={handleSubmit}
          />
        </div>
      </div>
    </Modal>
  );
}

export default DeletePersonModal;
