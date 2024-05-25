import {
  IoCallOutline,
  IoCopyOutline,
  IoSearchSharp,
  IoVideocamOutline,
} from "react-icons/io5";
import ChatVideoAndCall from "../../components/Modals/ChatVideoAndCallModal";
import { MenuSelect } from "../../components/Form";
import { FiEdit } from "react-icons/fi";
import { RiDeleteBin6Line } from "react-icons/ri";
import { BiDotsHorizontalRounded } from "react-icons/bi";
import { Link } from "react-router-dom";
import { convData } from "../../components/Datas";
import { LiaReplySolid } from "react-icons/lia";
import {
  MdOutlineImage,
  MdOutlineKeyboardVoice,
  MdOutlineLink,
} from "react-icons/md";
const DropDown1 = [
  {
    title: "Reply",
    icon: LiaReplySolid,
    onClick: (data) => {},
  },
  {
    title: "Copy",
    icon: IoCopyOutline,
    onClick: () => {},
  },
  {
    title: "Edit",
    icon: FiEdit,
    onClick: (data) => {},
  },
  {
    title: "Delete",
    icon: RiDeleteBin6Line,
    onClick: () => {},
  },
];

function Coversation() {
  const [isOpen, setIsOpen] = React.useState(false);
  const [video, setVideo] = React.useState(false);
  const closeModal = () => {
    setIsOpen(!isOpen);
  };
  return (
    <>
      {isOpen && (
        <ChatVideoAndCall
          isOpen={isOpen}
          closeModal={closeModal}
          video={video}
        />
      )}{" "}
      <div className="space-y-6">
        {/* head */}
        <div className="flex-btn gap-4 bg-white rounded-xl p-2 border border-gray-100">
          <div className="xs:block hidden">
            <div className="flex-rows gap-2 px-2 py-4">
              <Link to="/doctors/preview/1" className="relative">
                <img
                  className="rounded-full border object-cover w-10 h-10"
                  alt="user"
                  src="/images/user1.png"
                />
                <span className="w-[10px] h-[10px] border border-white bg-subMain rounded-full absolute top-0 right-0"></span>
              </Link>
              <div className="pl-2 space-y-1">
                <h2 className="font-medium text-xs">Minah mmassy</h2>
                <p className="text-textGray text-xs truncate">Active 4hr ago</p>
              </div>
            </div>
          </div>

          {/* buttones */}
          <div className="flex-rows xs:gap-2 gap-12">
            <button
              onClick={() => {
                setVideo(false);
                closeModal();
              }}
              className="w-10 h-10 rounded hover:bg-greyed flex-colo transitions text-xl"
            >
              <IoCallOutline />
            </button>
            <button
              onClick={() => {
                setVideo(true);
                closeModal();
              }}
              className="w-10 h-10 rounded hover:bg-greyed flex-colo transitions text-xl"
            >
              <IoVideocamOutline />
            </button>
            <button className="w-10 h-10 rounded hover:bg-greyed flex-colo transitions text-xl">
              <IoSearchSharp />
            </button>
          </div>
        </div>
        {/* conversation */}
        <div className="overflow-y-scroll space-y-4 sm:px-4 sm:max-h-[650px] max-h-[300px]">
          {convData.map((conv) => (
            <div
              id={conv?.id}
              className={`w-full flex gap-4 ${
                conv?.value?.me ? "flex-row-reverse" : ""
              }`}
            >
              <img
                src={conv?.user?.image}
                alt={conv?.user?.title}
                className="w-10 h-10 object-cover rounded-full"
              />
              <div className="space-y-1">
                <div
                  className={`py-3 rounded px-4 text-xs ${
                    conv?.value?.me
                      ? "bg-subMain text-white"
                      : "bg-white text-main border border-gray-100"
                  }`}
                >
                  {conv?.value?.image ? (
                    <img
                      src={conv?.imageUrl}
                      alt="user"
                      className="w-32 h-32 object-cover rounded"
                    />
                  ) : (
                    <p className="max-w-68 text-wrap leading-5">{conv?.text}</p>
                  )}
                </div>
                <p className="text-textGray text-xs">{conv?.time}</p>
              </div>
              <div className="">
                <MenuSelect datas={DropDown1} item={{}}>
                  <div className="text-textGray">
                    <BiDotsHorizontalRounded />
                  </div>
                </MenuSelect>
              </div>
            </div>
          ))}
        </div>
        {/* textarea */}
        <div className="grid grid-cols-12 gap-2 bg-white rounded p-4">
          <input
            className="xs:col-span-9 col-span-8 border text-xs border-border rounded py-4 px-2"
            placeholder="Write text here.."
          />
          <div className="xs:col-span-3 col-span-4 flex-btn gap-2">
            <button className="w-10 h-10 rounded hover:bg-greyed flex-colo transitions text-xl">
              <MdOutlineKeyboardVoice />
            </button>
            <button className="w-10 h-10 rounded hover:bg-greyed flex-colo transitions text-xl">
              <MdOutlineImage />
            </button>
            <button className="w-10 h-10 rounded hover:bg-greyed flex-colo transitions text-xl">
              <MdOutlineLink />
            </button>
            <button className="w-28 h-10 rounded bg-main text-white md:flex hidden justify-center items-center transitions text-xs">
              Send
            </button>
          </div>
        </div>
        <button className="w-full h-12 rounded bg-main text-white md:hidden flex justify-center items-center transitions text-xs">
          Send
        </button>
      </div>
    </>
  );
}

export default Coversation;
