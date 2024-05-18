/* eslint-disable no-unused-vars */
import React from 'react';
import { MdOutlineCloudDownload } from 'react-icons/md';
import { toast } from 'react-hot-toast';
import { BiPlus } from 'react-icons/bi';
import Layout from '../../Layout';
import { Button } from '../../components/Form';
import { DoctorsTable } from '../../components/Tables';
import { useNavigate } from 'react-router-dom';
import AddPersonModal from '../../components/Modals/AddPersonModal';
import { fetchPersonData } from '../../components/Datas';


function Doctors() {
  const [isOpen, setIsOpen] = React.useState(false);
  const [personsData, setPersonData] = React.useState([]);
  const [error, setError] = React.useState(null);
  const navigate = useNavigate();

  React.useEffect(() => {
    const loadpersonsData = async () => {
      try {
        const data = await fetchPersonData();
        const formattedData = data.map((item, index) => ({
          id: item.id,
          user: item,
          title: "Dr.",
        }));
        setPersonData(formattedData);
      } catch (error) {
        setError(error);
      }
    };

    loadpersonsData();
  }, []);

  const onCloseModal = () => {
    setIsOpen(false);
  };

  const preview = (data) => {
    navigate(`/doctors/preview/${data.id}`);
  };

  return (
    <Layout>
      {
        // add doctor modal
        isOpen && (
          <AddPersonModal
            closeModal={onCloseModal}
            isOpen={isOpen}
            doctor={true}
            datas={null}
          />
        )
      }
      {/* add button */}
      <button
        onClick={() => setIsOpen(true)}
        className="w-16 animate-bounce h-16 border border-border z-50 bg-subMain text-white rounded-full flex-colo fixed bottom-8 right-12 button-fb"
      >
        <BiPlus className="text-2xl" />
      </button>
      {/*  */}
      <h1 className="text-xl font-semibold">Persons</h1>
      <div
        data-aos="fade-up"
        data-aos-duration="1000"
        data-aos-delay="100"
        data-aos-offset="200"
        className="bg-white my-8 rounded-xl border-[1px] border-border p-5"
      >
        {/* datas */}

        <div className="grid md:grid-cols-6 sm:grid-cols-2 grid-cols-1 gap-2">
          <div className="md:col-span-5 grid lg:grid-cols-4 items-center gap-6">
            <input
              type="text"
              placeholder='Search "daudi mburuge"'
              className="h-14 w-full text-sm text-main rounded-md bg-dry border border-border px-4"
            />
          </div>

          {/* export */}
          <Button
            label="Export"
            Icon={MdOutlineCloudDownload}
            onClick={() => {
              toast.error('Exporting is not available yet');
            }}
          />
        </div>
        <div className="mt-8 w-full overflow-x-scroll">
          <DoctorsTable
            doctor={true}
            data={personsData}
            functions={{
              preview: preview,
            }}
          />
        </div>
      </div>
    </Layout>
  );
}

export default Doctors;
