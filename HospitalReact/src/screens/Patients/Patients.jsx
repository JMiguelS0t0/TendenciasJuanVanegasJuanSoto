import {useEffect, useState} from "react";
import Layout from "../../Layout/index.jsx";
import {Link, useNavigate} from "react-router-dom";
import {MdFilterList, MdOutlineCalendarMonth} from "react-icons/md";
import {toast} from "react-hot-toast";
import {Button} from "../../components/Form";
import {PatientTable} from "../../components/Tables";
import {loadPatientData} from "../../services/patientServices.js";
import {BiPlus} from "react-icons/bi";

function Patients() {
    const [patientData, setPatientData] = useState([]);
    const [error, setError] = useState(null);
    const [searchId, setSearchId] = useState("");
    const navigate = useNavigate();

    // preview
    const previewPayment = (id) => {
        navigate(`/patients/preview/${id}`);
    };

    const loadData = async () => {
        await loadPatientData(setPatientData, setError, searchId);
    }

    useEffect(() => {
        if (searchId === "") {
            loadData();
        }
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [searchId]);

    return (
        <Layout>
            {/* add button */}
            <Link
                to="/patients/create"
                className="w-16 animate-bounce h-16 border border-border z-50 bg-subMain text-white rounded-full flex-colo fixed bottom-8 right-12 button-fb"
            >
                <BiPlus className="text-2xl"/>
            </Link>
            <h1 className="text-xl font-semibold">Patients</h1>
            {/* datas */}
            <div
                data-aos="fade-up"
                data-aos-duration="1000"
                data-aos-delay="10"
                data-aos-offset="200"
                className="bg-white my-8 rounded-xl border-[1px] border-border p-5"
            >
                <div className="grid lg:grid-cols-5 grid-cols-1 xs:grid-cols-2 md:grid-cols-3 gap-2">
                    <input
                        type="text"
                        placeholder='Search "Patients"'
                        className="h-14 text-sm text-main rounded-md bg-dry border border-border px-4"
                    />
                    {/* export */}
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
                        }}
                        used={false}
                    />
                </div>
            </div>
        </Layout>
    );
}

export default Patients;
