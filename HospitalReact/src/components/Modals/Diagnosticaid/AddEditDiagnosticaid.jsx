/* eslint-disable no-unused-vars */
import {useEffect} from "react";
import Modal from "../Modal";
import {Button, Input} from "../../Form";
import {HiOutlineCheckCircle} from "react-icons/hi";
import {
    createDiagnostic,
    updateDiagnostic,
} from "../../../services/diagnosticaidServices.js";
import useField from "../../../hooks/useField";

function AddEditDiagnosticaidModal({
                                  closeModal,
                                  isOpen,
                                  datas,
                                  onDiagnosticAdded,
                              }) {
    const name = useField(datas?.name || "");
    const cost = useField(datas?.cost || "");

    const handleSubmit = async () => {
        if (datas?.id) {
            // Update medication
            await updateDiagnostic(datas.id, name.value, cost.value, closeModal);
        } else {
            // Create new medication
            await createDiagnostic(name.value, cost.value, closeModal);
        }
        onDiagnosticAdded();
    };

    useEffect(() => {
        if (datas) {
            name.onChange({target: {value: datas.name || ""}});
            cost.onChange({target: {value: datas.cost || ""}});
        }
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [datas]);

    return (
        <Modal
            closeModal={closeModal}
            isOpen={isOpen}
            title={datas?.name ? "Edit Diagnostic Aid" : "New Diagnostic Aid"}
            width={"max-w-3xl"}
        >
            <div className="flex-colo gap-6">
                <div className="grid sm:grid-cols-2 gap-4 w-full">
                    <Input
                        label="Dignostic aid"
                        color={true}
                        placeholder={datas?.name && datas.name}
                        name="name"
                        register={name}
                    />

                    <Input
                        label="cost (COP)"
                        type="number"
                        color={true}
                        placeholder={datas?.cost ? datas.cost : ""}
                        register={cost}
                    />
                </div>
                {/* buttones */}
                <div className="grid sm:grid-cols-2 gap-4 w-full">
                    <button
                        onClick={closeModal}
                        className="bg-red-600 bg-opacity-5 text-red-600 text-sm p-4 rounded-lg font-light"
                    >
                        {datas?.name ? "Discard" : "Cancel"}
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

export default AddEditDiagnosticaidModal;
