import {useState, useEffect} from "react";
import {BiPlus} from "react-icons/bi";
import Layout from "../Layout/index.jsx";
import {DiagnosticTable} from "../components/Tables";
import AddEditDiagnosticaidModal from "../components/Modals/Diagnosticaid/AddEditDiagnosticaid.jsx";
import DeleteDiagnosticaidModal from "../components/Modals/Diagnosticaid/DeleteDiagnosticaidModal.jsx";
import {loadDiagnostic} from "../services/diagnosticaidServices.js";

function DiagnosticAid() {
    const [isOpen, setIsOpen] = useState(false);
    const [isOpenDeleteModal, setIsOpenDeleteModal] = useState(false);
    const [data, setData] = useState([]);
    const [currentProcedure, setCurrentProcedure] = useState(null);
    // eslint-disable-next-line no-unused-vars
    const [error, setError] = useState(null);

    const loadData = async () => {
        await loadDiagnostic(setData, setError);
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
                <AddEditDiagnosticaidModal
                    isOpen={isOpen}
                    datas={currentProcedure}
                    closeModal={onCloseModal}
                    onDiagnosticAdded={loadData}
                />
            )}
            {/* DELETE MODAL */}
            {isOpenDeleteModal && (
                <DeleteDiagnosticaidModal
                    isOpen={isOpenDeleteModal}
                    datas={currentProcedure}
                    closeModal={onCloseDeleteModal}
                    onDiagnosticDelete={loadData}
                />
            )}
            {/* add button */}
            <button
                onClick={() => setIsOpen(true)}
                className="w-16 animate-bounce h-16 border border-border z-50 bg-subMain text-white rounded-full flex-colo fixed bottom-8 right-12 button-fb"
            >
                <BiPlus className="text-2xl"/>
            </button>
            {/*  */}
            <h1 className="text-xl font-semibold">Diagnostic Aid</h1>
            <div
                data-aos="fade-up"
                data-aos-duration="1000"
                data-aos-delay="100"
                data-aos-offset="200"
                className="bg-white my-8 rounded-xl border-[1px] border-border p-5"
            >
                <div className="mt-8 w-full overflow-x-scroll">
                    <DiagnosticTable data={data} onEdit={onEdit} onDelete={onDelete}/>
                </div>
            </div>
        </Layout>
    );
}

export default DiagnosticAid;
