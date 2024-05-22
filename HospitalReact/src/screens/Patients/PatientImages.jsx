/* eslint-disable no-unused-vars */
import { FaTimes } from "react-icons/fa";
import { toast } from "react-hot-toast";
import Uploader from "../../components/Uploader";
import { Button } from "../../components/Form";
import { patientImages } from "../../components/Datas";
import { useState } from "react";

function PatientImages() {
  const [image, setImage] = useState(null);
  return (
    <div className="flex-colo gap-8">
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4 w-full">
        {patientImages?.map((image, i) => (
          <div key={i} className="relative w-full">
            <img
              src={image}
              alt="patient"
              className="w-full h-72 rounded-lg object-cover"
            />
            <button
              onClick={() => toast.error("This feature is not available yet.")}
              className="bg-white rounded-full w-8 h-8 flex-colo absolute -top-1 -right-1"
            >
              <FaTimes className="text-red-500" />
            </button>
          </div>
        ))}
      </div>
      <Uploader setImage={setImage} />
      <Button
        onClick={() => toast.error("This feature is not available yet.")}
        label="Save Changes"
        Icon={null}
      />
    </div>
  );
}

export default PatientImages;
