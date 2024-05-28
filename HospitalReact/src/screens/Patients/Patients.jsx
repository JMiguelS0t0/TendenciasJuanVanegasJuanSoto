// Patients.jsx
import { useEffect, useState } from "react";
import Layout from "../../Layout/index.jsx";
import { Link, useNavigate } from "react-router-dom";
import { MdFilterList } from "react-icons/md";
import { toast } from "react-hot-toast";
import { Button } from "../../components/Form";
import { PatientTable } from "../../components/Tables";
import { loadPatientData } from "../../services/patientServices.js";
import { BiPlus } from "react-icons/bi";
import DeletePatientModal from "../../components/Modals/DeletePatientModal.jsx";

function Patients() {
    const [patientData, setPatientData] = useState([]);
    const [error, setError] = useState(null);
    const [searchId, setSearchId] = useState("");
    const [selectedPatientId, setSelectedPatientId] = useState(null); // Nuevo estado para almacenar el ID del paciente seleccionado para eliminar
    const [isDeleteModalOpen, setIsDeleteModalOpen] = useState(false); // Estado para controlar la apertura del modal de eliminación
    const navigate = useNavigate();

    // Vista previa
    const previewPayment = (id) => {
        navigate(`/patients/preview/${id}`);
    };

    const loadData = async () => {
        await loadPatientData(setPatientData, setError, searchId);
    };

    useEffect(() => {
        if (searchId === "") {
            loadData();
        }
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [searchId]);

    const handleDelete = async (id) => {
        setSelectedPatientId(id);
        setIsDeleteModalOpen(true);
    };

    return (
        <Layout>
            {/* Botón de agregar */}
            <Link
                to="/patients/create"
                className="w-16 animate-bounce h-16 border border-border z-50 bg-subMain text-white rounded-full flex-colo fixed bottom-8 right-12 button-fb"
            >
                <BiPlus className="text-2xl"/>
            </Link>
            <h1 className="text-xl font-semibold">Patients</h1>
            {/* Datos */}
            <div className="bg-white my-8 rounded-xl border-[1px] border-border p-5">
                <div className="grid lg:grid-cols-5 grid-cols-1 xs:grid-cols-2 md:grid-cols-3 gap-2">
                    <input
                        type="text"
                        placeholder='Search "Patients"'
                        className="h-14 text-sm text-main rounded-md bg-dry border border-border px-4"
                    />
                    {/* Exportar */}
                    <Button
                        label="Filter"
                        Icon={MdFilterList}
                        onClick={() => {
                            toast.error("Filter data is not available yet");
                        }}
                    />
                </div>
                <div className="mt-8 w-full overflow-x-scroll">
                    <PatientTable
                        data={patientData}
                        functions={{
                            preview: previewPayment,
                            onDelete: handleDelete,
                        }}
                        used={false}
                    />
                </div>
                {/* Modal de eliminación */}
                <DeletePatientModal
                    isOpen={isDeleteModalOpen}
                    closeModal={() => setIsDeleteModalOpen(false)}
                    patientId={selectedPatientId}
                    onDeleteSuccess={() => {
                        setIsDeleteModalOpen(false);
                        loadData();
                    }}
                />
            </div>
        </Layout>
    );
}

export default Patients;
