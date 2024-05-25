import { chatsData } from "../../components/Datas";
import { LuMessageSquarePlus } from "react-icons/lu";

function SideBarChat() {
  return (
    <div className="space-y-6">
      <h3 className="text-sm font-semibold">
        Messages
        <span className="text-white text-xs px-2 py-1 ml-2 bg-subMain rounded-full">
          3
        </span>
      </h3>
      {/* search */}
      <div className="grid grid-cols-12 gap-2">
        <input
          type="text"
          placeholder="Search"
          className="col-span-10 bg-transparent border border-border rounded-lg px-2 py-3 text-xs"
        />
        <button className="w-10 h-10 rounded bg-subMain text-white flex-colo transitions text-md">
          <LuMessageSquarePlus />
        </button>
      </div>

      {/* users */}
      <div className=" overflow-y-scroll z-0 relative xl:max-h-[780px] max-h-[200px]">
        {chatsData.map((chat, i) => (
          <div
            key={i}
            className="grid cursor-pointer grid-cols-12 gap-2 px-2 py-4 hover:bg-text transitions hover:rounded border-b border-border"
          >
            <div className="col-span-2 relative">
              <img
                className="rounded-full border object-cover w-10 h-10"
                alt="user"
                src={chat?.user?.image}
              />
              {chat?.status && (
                <span className="w-[10px] h-[10px] border border-white bg-subMain rounded-full absolute top-0 right-0"></span>
              )}
            </div>
            <div className="col-span-7 pl-2 space-y-1">
              <h2 className="font-medium text-xs">{chat?.user?.title}</h2>
              <p className="text-textGray text-xs truncate">{chat?.message}</p>
            </div>
            <div className="col-span-3">
              <p className="text-textGray text-[11px]">{chat?.active}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default SideBarChat;
