import {useEffect} from "react";
import Modal from "../Modal";
import {Button, Input} from "../../Form";
import {HiOutlineCheckCircle} from "react-icons/hi";
import {
    createProcedure,
    updateProcedureData,
} from "../../../services/procedureServices.js";
import useField from "../../../hooks/useField";


function AddEditProcedureModal({
                                   closeModal,
                                   isOpen,
                                   datas,
                                   onProcedureAdded,
                               }) {
    const name = useField(datas?.name || "");
    const cost = useField(datas?.price || "");

    const handleSubmit = async () => {
        if (datas?.id) {
            await updateProcedureData(datas.id, name.value, cost.value, closeModal);
        } else {
            await createProcedure(name.value, cost.value, closeModal);
        }
        onProcedureAdded();
    };

    useEffect(() => {
        if (datas) {
            name.onChange({target: {value: datas.name || ""}});
            cost.onChange({target: {value: datas.cost || ""}});
        }
    }, [datas]);

    return (
        <Modal
            closeModal={closeModal}
            isOpen={isOpen}
            title={datas?.name ? "Edit Procedure" : "New Procedure"}
            width={"max-w-3xl"}
        >
            <div className="flex-colo gap-6">
                <Input
                    label="Procedure Name"
                    color={true}
                    placeholder={datas?.name && datas.name}
                    name="name"
                    register={name}
                />

                <Input
                    label="Price (COP)"
                    type="number"
                    color={true}
                    placeholder={datas?.cost ? datas.cost : ""}
                    register={cost}
                />

                {/* buttons */}
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

export default AddEditProcedureModal;
