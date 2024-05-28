import Modal from "./Modal";
import {Button} from "../Form.jsx";
import {HiOutlineCheckCircle} from "react-icons/hi";
import {toast} from "react-hot-toast";

import {handleDelete} from "../../services/patientServices.js";

function DeletePatientModal({closeModal, isOpen, patientId, onDeleteSuccess}) {
    const handleSubmit = async () => {
        try {
            await handleDelete(patientId);
            toast.success("Patient deleted successfully");
            onDeleteSuccess();
        } catch (error) {
            console.error("Error: ", error);
            toast.error("Error deleting patient");
        }
        closeModal();
    };

    return (
        <Modal
            closeModal={closeModal}
            isOpen={isOpen}
            title={"Delete Patient"}
            width={"max-w-3xl"}
        >
            <div className="flex-colo gap-6">
                <p>
                    ¿Estás seguro que deseas eliminar al paciente?
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

export default DeletePatientModal;
