import Modal from "../Modal";
import { Button } from "../../Form";
import { HiOutlineCheckCircle } from "react-icons/hi";
import { toast } from "react-hot-toast";

import {deleteMedication} from "../../../services/medicationServices";

function DeleteMedicationModal({closeModal, isOpen, datas, onMedicationDelete}){
    const handleSubmit = async () => {
        try{
            await deleteMedication(datas);
        } catch (error) {
            console.log("Error: ", error);
            toast.error("Error deleting medication");
        }
        closeModal();
        onMedicationDelete();
    };

    return (
        <Modal
          closeModal={closeModal}
          isOpen={isOpen}
          title={"Delete Medication"}
          width={"max-w-3xl"}
        >
          <div className="flex-colo gap-6">
            <p>
              ¿Estás seguro que deseas eliminar el medicamento?
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

export default DeleteMedicationModal;