import { MenuDatas } from "../components/Datas";
import { Link } from "react-router-dom";

function Sidebar() {
  // active link
  const currentPath = (path) => {
    const currentPath =
      window.location.pathname.split("/")[1] === path.split("/")[1];
    if (currentPath) {
      return path;
    }
    return null;
  };

  return (
    <div className="bg-white xl:shadow-lg px-4 xl:h-screen w-full border-r border-border">
      <Link to="/">
        <img
          src="/images/logo.png"
          alt="logo"
          className="w-3/4 h-12 ml-4 object-contain"
        />
      </Link>
      <div className="flex-colo gap-2 mt-6">
        {MenuDatas.map((item, index) => (
          <Link
            to={item.path}
            key={index}
            className={`
            ${currentPath(item.path) === item.path ? "bg-text" : ""}
            flex gap-4 transitions group items-center w-full p-4 rounded-lg hover:bg-text`}
          >
            <item.icon
              className={`text-xl text-subMain
            `}
            />
            <p
              className={`text-sm font-medium group-hover:text-subMain ${
                currentPath(item.path) === item.path
                  ? "text-subMain"
                  : "text-gray-500"
              }`}
            >
              {item.title}
            </p>
          </Link>
        ))}
      </div>
    </div>
  );
}

export default Sidebar;
