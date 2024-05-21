import { HiOutlineHome, HiOutlineMail, HiOutlineUsers } from "react-icons/hi";
import {
  TbCalendar,
  TbChartHistogram,
  TbFile,
  TbFileInvoice,
  TbLockAccess,
  TbUsers,
} from "react-icons/tb";
import { FaRegCalendarAlt, FaTelegramPlane, FaWhatsapp } from "react-icons/fa";
import {
  RiFileList3Line,
  RiHeartLine,
  RiImageLine,
  RiLockPasswordLine,
  RiMedicineBottleLine,
  RiMoneyDollarCircleLine,
  RiStethoscopeLine,
  RiUserHeartLine,
  RiUserLine,
} from "react-icons/ri";
import {
  MdListAlt,
  MdOutlineAttachMoney,
  MdOutlineInventory2,
  MdOutlineReviews,
  MdOutlineTextsms,
} from "react-icons/md";
import { BiCalendar, BiUserPlus } from "react-icons/bi";

export const MenuDatas = [
  {
    title: "Dashboard",
    path: "/",
    icon: HiOutlineHome,
  },
  {
    title: "Patients",
    path: "/patients",
    icon: TbUsers,
  },
  {
    title: "Receptions",
    path: "/receptions",
    icon: HiOutlineUsers,
  },
  {
    title: "Doctors",
    path: "/doctors",
    icon: RiUserHeartLine,
  },

  {
    title: "Appointments",
    path: "/appointments",
    icon: FaRegCalendarAlt,
  },
  {
    title: "Payments",
    path: "/payments",
    icon: MdListAlt,
  },
  {
    title: "Invoices",
    path: "/invoices",
    icon: TbFileInvoice,
  },
  {
    title: "Procedures",
    path: "/services", //ORGANIZAR ESTO
    icon: MdOutlineInventory2,
  },
  {
    title: "Medicine",
    path: "/medicine",
    icon: RiMedicineBottleLine,
  },
  // {
  //   title: "Settings",
  //   path: "/settings",
  //   icon: AiOutlineSetting,
  // },
];

export const memberData = [
  {
    id: 1,
    title: "Hugo Lloris",
    image: "/images/user1.png",
    admin: false,
    email: "hugolloris@gmail.com",
    phone: "+1 234 567 890",
    age: 25,
    gender: "Male",
    blood: "A+",
    totalAppointments: 5,
    date: "20 Aug 2021",
  },
  {
    id: 2,
    title: "Mauris auctor",
    image: "/images/user2.png",
    admin: false,
    email: "maurisauctor@gmail.com",
    phone: "+1 456 789 123",
    age: 34,
    gender: "Female",
    blood: "B+",
    totalAppointments: 3,
    date: "22 Nov 2023",
  },
  {
    id: 3,
    title: "Michael Owen",
    image: "/images/user3.png",
    admin: false,
    phone: "+1 890 123 456",
    email: "michaelowen@gmail.com",
    age: 45,
    gender: "Male",
    blood: "O+",
    totalAppointments: 26,
    date: "12 Jan 2020",
  },
  {
    id: 4,
    title: "Amina Smith",
    image: "/images/user4.png",
    admin: true,
    phone: "+1 908 765 432",
    email: "aminasmith@gmail.com",
    age: 28,
    gender: "Female",
    blood: "AB+",
    totalAppointments: 17,
    date: "07 Feb 2001",
  },
  {
    id: 5,
    title: "Minahil Khan",
    image: "/images/user5.png",
    admin: false,
    phone: "+1 890 123 456",
    email: "minahilkhan@gmail.com",
    age: 35,
    gender: "Female",
    blood: "A+",
    totalAppointments: 9,
    date: "30 Dec 2019",
  },
  {
    id: 6,
    title: "Alex Morgan",
    image: "/images/user6.png",
    admin: false,
    phone: "+1 908 765 432",
    email: "alexmorgan@gmail.com",
    age: 29,
    gender: "Male",
    blood: "B+",
    totalAppointments: 34,
    date: "12 Jan 2020",
  },
  {
    id: 7,
    title: "John Doe",
    image: "/images/user7.png",
    admin: false,
    phone: "+1 234 567 890",
    email: "johndoe@gmail.com",
    age: 32,
    gender: "Male",
    blood: "O-",
    totalAppointments: 12,
    date: "18 Mar 2023",
  },
  {
    id: 8,
    title: "David Beckham",
    image: "/images/user8.png",
    admin: false,
    phone: "+1 456 789 123",
    email: "davidbackham@gmail.com",
    age: 27,
    gender: "Female",
    blood: "AB+",
    totalAppointments: 70,
    date: "01 June 2018",
  },
];
export const medicineData = [
  {
    id: 1,
    name: "Paracetamol",
    measure: "Tablet",
    stock: 400,
    price: 1000,
    status: "Available",
    instraction: "After meal",
  },
  {
    id: 2,
    name: "Amoxicillin",
    measure: "Capsule",
    stock: 200,
    price: 2300,
    status: "Available",
    instraction: "After meal",
  },
  {
    id: 3,
    name: "Ibuprofen",
    measure: "mm",
    stock: 0,
    price: 5000,
    status: "Out of stock",
    instraction: "Before meal",
  },
  {
    id: 4,
    name: "Aspirin",
    measure: "cm",
    stock: 370,
    price: 3500,
    status: "Available",
    instraction: "After meal",
  },
  {
    id: 5,
    name: "Diazepam",
    measure: "gm",
    stock: 0,
    price: 12000,
    status: "Out of stock",
    instraction: "Before meal",
  },
  {
    id: 6,
    name: "Lorazepam",
    measure: "mg",
    stock: 123,
    price: 15500,
    status: "Available",
    instraction: "Before meal",
  },
  {
    id: 7,
    name: "Codeine",
    measure: "ml",
    stock: 1,
    price: 30000,
    status: "Available",
    instraction: "After meal",
  },
  {
    id: 8,
    name: "Tramadol",
    measure: "lb",
    stock: 0,
    price: 200,
    status: "Out of stock",
    instraction: "Before meal",
  },
];

export const sortsDatas = {
  status: [
    {
      id: 1,
      name: "Status...",
    },
    {
      id: 2,
      name: "Pending",
    },
    {
      id: 3,
      name: "Approved",
    },
    {
      id: 4,
      name: "Cancelled",
    },
  ],
  method: [
    {
      id: 1,
      name: "Payment method",
    },
    {
      id: 2,
      name: "Cash",
    },
    {
      id: 3,
      name: "Allianz Insurance",
    },
    {
      id: 4,
      name: "Cigna Insurance",
    },
    {
      id: 5,
      name: "Humana Insurance",
    },
    {
      id: 6,
      name: "Axa Insurance",
    },
    {
      id: 7,
      name: "GeoBlue Insurance",
    },
  ],
  currency: [
    {
      id: 1,
      name: "Select Currency",
    },
    {
      id: 2,
      name: "USD (US Dollar)",
    },
    {
      id: 3,
      name: "EUR (Euro)",
    },
    {
      id: 4,
      name: "TSH (Tanzanian Shilling)",
    },
  ],
  instractions: [
    {
      id: 1,
      name: "Select Instraction",
    },
    {
      id: 2,
      name: "After Meal",
    },
    {
      id: 3,
      name: "Before Meal",
    },
  ],
  measure: [
    {
      id: 1,
      name: "Select Measure",
    },
    {
      id: 2,
      name: "mg",
    },
    {
      id: 3,
      name: "ml",
    },
    {
      id: 4,
      name: "gm",
    },
    {
      id: 5,
      name: "kg",
    },
    {
      id: 6,
      name: "lb",
    },
    {
      id: 7,
      name: "tbsp",
    },
    {
      id: 8,
      name: "tablet",
    },
    {
      id: 9,
      name: "capsule",
    },
  ],
  stocks: [
    {
      id: 1,
      name: "All",
    },
    {
      id: 2,
      name: "Available",
    },
    {
      id: 3,
      name: "Out of Stock",
    },
  ],
  service: [
    {
      id: 1,
      name: "All",
    },
    {
      id: 2,
      name: "Enabled",
    },
    {
      id: 3,
      name: "Disabled",
    },
  ],
  roles: [
    {
      id: 1,
      name: "Admin",
    },
    {
      id: 2,
      name: "Doctor",
    },
    {
      id: 3,
      name: "Nurse",
    },
    {
      id: 4,
      name: "Support",
    },
  ],
  filterPatient: [
    {
      id: 1,
      name: "Sort by...",
    },
    {
      id: 2,
      name: "Newest Patients",
    },
    {
      id: 3,
      name: "Oldest Patients",
    },
  ],
  genderFilter: [
    {
      id: 1,
      name: "Gender...",
    },
    {
      id: 2,
      name: "Female",
    },
    {
      id: 3,
      name: "Male",
    },
  ],
  bloodTypeFilter: [
    {
      id: 1,
      name: "Blood Type...",
    },
    {
      id: 2,
      name: "A+",
    },
    {
      id: 3,
      name: "A-",
    },
    {
      id: 4,
      name: "B+",
    },
    {
      id: 5,
      name: "B-",
    },
    {
      id: 6,
      name: "AB+",
    },
    {
      id: 7,
      name: "AB-",
    },
    {
      id: 8,
      name: "O+",
    },
    {
      id: 9,
      name: "O-",
    },
  ],
  dosage: [
    {
      id: 1,
      name: "Morning (M)",
      value: "morning",
    },
    {
      id: 2,
      name: "Afternoon (A)",
      value: "afternoon",
    },
    {
      id: 3,
      name: "Evening (E)",
      value: "evening",
    },
  ],
  star: [
    {
      id: 1,
      name: "Filter by Rating",
      value: "all",
    },
    {
      id: 1,
      name: "0 - Very Bad",
      value: 0,
    },
    {
      id: 2,
      name: "1 - Bad",
      value: 1,
    },
    {
      id: 3,
      name: "2 - Good",
      value: 2,
    },
    {
      id: 4,
      name: "3 - Very Good",
      value: 3,
    },
    {
      id: 5,
      name: "4 - Excellent",
      value: 4,
    },
    {
      id: 6,
      name: "5 - Master",
      value: 5,
    },
  ],
  users: [
    {
      id: 1,
      name: "Filter by ...",
      value: "all",
    },
    {
      id: 2,
      name: "Doctors",
      value: "doctors",
    },
    {
      id: 3,
      name: "Hospital",
      value: "hospital",
    },
    {
      id: 4,
      name: "Products",
      value: "products",
    },
  ],
};

export const campaignData = [
  {
    id: 1,
    title: "Offer on Dental Checkup",
    date: "3 days ago",
    type: "email",
    sendTo: "All Patients",
    action: {
      subject: "Delight patients with a free dental checkup",
      message:
        "Dear Patient, We are delighted to offer you a free dental checkup. Please visit our clinic to avail this offer. Thank you. and have a nice day. and welcome to our clinic.",
      subHeader: "Offer on Dental Checkup",
      header: "How to avail this offer?",
      footer: "This offer is valid till 30th June, 2021",
    },
  },
  {
    id: 2,
    title: "Britam Insurance Offer",
    date: "8 days ago",
    type: "whatsapp",
    sendTo: "Britam Patients",
    action: {
      message:
        "Hellow Patient, are you looking for a free dental checkup? We are delighted to offer you a free dental checkup. Please visit our clinic to avail this offer. Thank you.",
    },
  },
  {
    id: 3,
    title: "NHCF Insurance Offer",
    date: "10 days ago",
    type: "sms",
    sendTo: "NHCF Patients",
    action: {
      message:
        "Hola, Delight patient with NHCF Insurance, We are delighted to offer you a free dental checkup. Please visit our clinic to avail this offer. Thank you.",
    },
  },
  {
    id: 4,
    title: "Cash patients offer",
    date: "15 days ago",
    type: "sms",
    sendTo: "Cash Patients",
    action: {
      message:
        "Delight Patient, now get 50% off on dental checkup. Please visit our clinic to avail this offer. Thank you. and have a nice day. and welcome to our clinic.",
    },
  },
  {
    id: 5,
    title: "Braces Offer",
    date: "12 days ago",
    type: "email",
    sendTo: "Britam Patients",
    action: {
      subject: "Delight patients with a free dental checkup",
      message:
        "Dear Patient, Britam Insurance is delighted to offer you a free dental checkup. Please visit our clinic to avail this offer. Thank you. and have a nice day. and welcome to our clinic.",
      subHeader: "Braces Offer for Britam Patients",
      header: "Now get braces at 50% off",
      footer: "This offer is valid till 30th June, 2021",
    },
  },
  {
    id: 6,
    title: "Teeth Whitening Offer",
    date: "20 days ago",
    type: "whatsapp",
    sendTo: "All Patients",
    action: {
      message:
        "Hola, Delight patient with Teeth Whitening Offer, We are delighted to offer you a free dental checkup. Please visit our clinic to avail this offer. Thank you.",
    },
  },
];
export const servicesData = [
  {
    id: 1,
    name: "Select service.. ",
  },
  {
    id: 2,
    name: "Refractive Lens Exchange (RLE)",
    price: 40000,
    date: "23 June, 2021",
    status: true,
  },
  {
    id: 3,
    name: "Cataracts Surgery",
    price: 20000,
    date: "12 Jan, 2022",
    status: true,
  },
  {
    id: 4,
    name: "Lasik and Lasek (PRK)",
    price: 50000,
    date: "11 April, 2023",
    status: false,
  },
  {
    id: 5,
    name: "Implantable Contact Lens (ICL)",
    price: 34000,
    date: "10 Agst, 2021",
    status: true,
  },
  {
    id: 6,
    name: "Corneal Human Inlays (KeraNatural)",
    price: 10400,
    date: "23 June, 2021",
    status: false,
  },
  {
    id: 7,
    name: "Corneal Cross Linking (CXL)",
    price: 150000,
    date: "09 Dec, 2023",
    status: false,
  },
  {
    id: 8,
    name: "Dry Eye Treatment",
    price: 23000,
    date: "05 Feb, 2019",
    status: true,
  },
  {
    id: 9,
    name: "Amblyopia (Bynocs)",
    price: 40000,
    date: "16 Nov, 2022",
    status: true,
  },
  {
    id: 10,
    name: "Drooping Eyelids",
    price: 19000,
    date: "02 Jun, 2022",
    status: false,
  },
  {
    id: 11,
    name: "Paeditaric Ophthalmology",
    price: 160000,
    date: "23 June, 2021",
    status: true,
  },
];

export const invoicesData = [
  {
    id: 206719,
    to: memberData[5],
    total: 6070,
    createdDate: "12/06/2021",
    dueDate: "16/06/2021",
    items: [
      {
        id: 1,
        name: servicesData[0].name,
        price: 500,
        description: "",
      },
      {
        id: 2,
        name: servicesData[1].name,
        price: 300,
        description: "",
      },
      {
        id: 3,
        name: medicineData[2].name,
        price: 260,
        description: "",
      },
      {
        id: 4,
        name: medicineData[0].name,
        price: 190000,
        description: "",
      },
      {
        id: 5,
        name: servicesData[4].name,
        price: 15000,
        description: "",
      },
    ],
  },
  {
    id: 198772,
    to: memberData[6],
    total: 5000,
    createdDate: "10/02/2023",
    dueDate: "14/02/2023",
    items: [
      {
        id: 1,
        name: servicesData[3].name,
        price: 190000,
        description: "",
      },
      {
        id: 2,
        name: medicineData[4].name,
        price: 15000,
        description: "",
      },
      {
        id: 3,
        name: servicesData[8].name,
        price: 20000,
        description: "",
      },
      {
        id: 4,
        name: medicineData[3].name,
        price: 190000,
        description: "",
      },
    ],
  },
  {
    id: 456789,
    to: memberData[7],
    total: 10000,
    createdDate: "09/01/2023",
    dueDate: "13/01/2023",
    items: [
      {
        id: 1,
        name: servicesData[5].name,
        price: 5000,
        description: "",
      },
      {
        id: 2,
        name: medicineData[6].name,
        price: 16000,
        description: "",
      },
      {
        id: 3,
        name: medicineData[7].name,
        price: 10000,
        description: "",
      },
      {
        id: 4,
        name: medicineData[2].name,
        price: 20000,
        description: "",
      },
    ],
  },
  {
    id: 876543,
    to: memberData[4],
    total: 19000,
    createdDate: "08/01/2023",
    dueDate: "12/01/2023",
    items: [
      {
        id: 1,
        name: medicineData[5].name,
        price: 5000,
        description: "",
      },
      {
        id: 2,
        name: servicesData[6].name,
        price: 16000,
        description: "",
      },
      {
        id: 3,
        name: servicesData[7].name,
        price: 10000,
        description: "",
      },
      {
        id: 4,
        name: medicineData[1].name,
        price: 20000,
        description: "",
      },
      {
        id: 5,
        name: servicesData[3].name,
        price: 190000,
        description: "",
      },
      {
        id: 6,
        name: servicesData[4].name,
        price: 15000,
        description: "",
      },
    ],
  },
];

export const appointmentsData = [
  {
    id: 1,
    time: "2 hrs later",
    user: memberData[4],
    from: "10:00 AM",
    to: "12:00 PM",
    hours: 2,
    status: "Pending",
    doctor: memberData[0],
    date: "Jun 12, 2021",
  },
  {
    id: 2,
    time: "1 hrs ago",
    user: memberData[5],
    from: "13:00 Pm",
    to: "18:00 PM",
    hours: 5,
    status: "Cancel",
    doctor: memberData[1],
    date: "Feb 24, 2021",
  },
  {
    id: 3,
    time: "2 hrs ago",
    user: memberData[6],
    from: "10:00 AM",
    to: "12:00 PM",
    hours: 2,
    status: "Approved",
    doctor: memberData[2],
    date: "Mar 12, 2023",
  },
  {
    id: 4,
    time: "3 hrs later",
    user: memberData[7],
    from: "06:00 AM",
    to: "08:00 AM",
    hours: 3,
    status: "Pending",
    doctor: memberData[3],
    date: "Apr 06, 2023",
  },
  {
    id: 5,
    time: "4 hrs ago",
    user: memberData[3],
    from: "10:00 AM",
    to: "12:00 PM",
    hours: 7,
    status: "Approved",
    doctor: memberData[4],
    date: "May 18, 2023",
  },
];

export const transactionData = [
  {
    id: 1,
    user: memberData[0],
    date: "Mar 12, 2022",
    amount: 1000,
    status: "Paid",
    method: "Cash",
    doctor: memberData[3],
  },
  {
    id: 2,
    user: memberData[1],
    date: "Agus 12, 2023",
    amount: 2300,
    status: "Paid",
    method: "NHCF",
    doctor: memberData[4],
  },
  {
    id: 3,
    user: memberData[2],
    date: "Jan 06, 2024",
    amount: 1200,
    status: "Pending",
    method: "Britam",
    doctor: memberData[5],
  },
  {
    id: 4,
    user: memberData[3],
    date: "Feb 18, 2025",
    amount: 1400,
    status: "Cancel",
    method: "NHCF",
    doctor: memberData[6],
  },
  {
    id: 5,
    user: memberData[4],
    date: "Mar 12, 2026",
    amount: 1230,
    status: "Pending",
    method: "Cash",
    doctor: memberData[7],
  },
  {
    id: 6,
    user: memberData[5],
    date: "Apr 12, 2027",
    amount: 1000,
    status: "Paid",
    method: "NHCF",
    doctor: memberData[0],
  },
  {
    id: 7,
    user: memberData[6],
    date: "May 12, 2028",
    amount: 8900,
    status: "Cancel",
    method: "Britam",
    doctor: memberData[1],
  },
  {
    id: 8,
    user: memberData[7],
    date: "Jun 12, 2029",
    amount: 1000,
    status: "Pending",
    method: "Britam",
    doctor: memberData[2],
  },
];

export const dashboardCards = [
  {
    id: 1,
    title: "Total Patients",
    icon: TbUsers,
    value: 1600,
    percent: 45.06,
    color: ["bg-subMain", "text-subMain", "#07b8db"],
    datas: [92, 80, 45, 15, 49, 77, 70, 51, 110, 20, 90, 60],
  },
  {
    id: 2,
    title: "Appointments",
    icon: TbCalendar,
    value: 130,
    percent: 25.06,
    color: ["bg-yellow-500", "text-yellow-500", "#F9C851"],
    datas: [20, 50, 75, 15, 108, 97, 70, 41, 50, 20, 90, 60],
  },
  {
    id: 3,
    title: "Prescriptions",
    icon: TbFile,
    value: 4160,
    percent: 65.06,
    color: ["bg-[#66B5A3]", "text-[#66B5A3]", "#66B5A3"],
    datas: [92, 80, 45, 15, 49, 77, 70, 51, 110, 20, 90, 60],
  },
  {
    id: 4,
    title: "Total Earnings",
    icon: MdOutlineAttachMoney,
    value: 4590,
    percent: 45.06,
    color: ["bg-[#e6870b]", "text-[#e6870b]", "#e6870b"],
    datas: [20, 50, 75, 15, 108, 97, 70, 41, 50, 20, 90, 60],
  },
];

export const notificationsData = [
  {
    id: 1,
    action: 1,
    user: memberData[0],
    time: "2 hours ago",
  },
  {
    id: 2,
    action: 2,
    user: memberData[1],
    time: "2 days ago",
  },
  {
    id: 3,
    action: 1,
    user: memberData[2],
    time: "3 days ago",
  },
  {
    id: 4,
    action: 2,
    user: memberData[3],
    time: "4 days ago",
  },
];

export const shareData = [
  {
    id: 1,
    icon: HiOutlineMail,
    title: "Email",
    description: "Send to patient email address",
  },
  {
    id: 2,
    icon: MdOutlineTextsms,
    title: "SMS",
    description: "Send to patient phone number",
  },
  {
    id: 3,
    icon: FaWhatsapp,
    title: "WhatsApp",
    description: "Send to patient WhatsApp account",
  },
  {
    id: 4,
    icon: FaTelegramPlane,
    title: "Telegram",
    description: "Send to patient Telegram account",
  },
];

export const patientTab = [
  {
    id: 1,
    title: "Medical Records",
    icon: TbChartHistogram,
  },
  {
    id: 2,
    title: "Appointments",
    icon: BiCalendar,
  },
  {
    id: 3,
    title: "Invoices",
    icon: RiFileList3Line,
  },
  {
    id: 4,
    title: "Payments",
    icon: RiMoneyDollarCircleLine,
  },
  {
    id: 5,
    title: "Images",
    icon: RiImageLine,
  },
  {
    id: 6,
    title: "Chart",
    icon: RiStethoscopeLine,
  },
  {
    id: 7,
    title: "Patient Information",
    icon: RiUserLine,
  },
  {
    id: 8,
    title: "Health Information",
    icon: RiHeartLine,
  },
];

export const doctorTab = [
  {
    id: 1,
    title: "Personal Information",
    icon: RiUserLine,
  },
  {
    id: 2,
    title: "Patients",
    icon: BiUserPlus,
  },
  {
    id: 3,
    title: "Appointments",
    icon: BiCalendar,
  },
  {
    id: 4,
    title: "Payments",
    icon: RiMoneyDollarCircleLine,
  },
  {
    id: 5,
    title: "Invoices",
    icon: RiFileList3Line,
  },
  {
    id: 6,
    title: "Reviews",
    icon: MdOutlineReviews,
  },
  {
    id: 7,
    title: "Access Control",
    icon: TbLockAccess,
  },
  {
    id: 8,
    title: "Change Password",
    icon: RiLockPasswordLine,
  },
];

export const medicalRecodData = [
  {
    id: 1,
    date: "13, Jan 2021",
    amount: 150000,
    data: [
      {
        id: 1,
        title: "Complaint",
        value: "Sudden loss of vision,Red eyes,Double vision,Blurred vision",
      },
      {
        id: 2,
        title: "Diagnosis",
        value: "High blood pressure, Diabetes, Hypertension",
      },
      {
        id: 3,
        title: "Treatment",
        value: "Refractive Lens Exchange (RLE)",
      },
      {
        id: 4,
        title: "Prescription",
        value: "Paracetamol, Amoxicillin, Ibuprofen, Aspirin",
      },
    ],
    attachments: [
      "https://placehold.it/300x300",
      "https://placehold.it/300x300",
      "https://placehold.it/300x300",
      "https://placehold.it/300x300",
    ],
    vitalSigns: [
      "Blood Pressure: 120/80 mmHg",
      "Pulse Rate: 80 bpm",
      "Respiratory Rate: 16 bpm",
      "Temperature: 36.5 °C",
      "Oxygen Saturation: 98%",
    ],
  },
  {
    id: 2,
    date: "10, Feb 2022",
    amount: 300000,
    data: [
      {
        id: 1,
        title: "Complaint",
        value: "Flashing lights and floaters,Watery eyes,Painful vision",
      },
      {
        id: 2,
        title: "Diagnosis",
        value: "High cholesterol,Rheumatoid arthritis",
      },
      {
        id: 3,
        title: "Treatment",
        value: "Cataracts Surgery, Laser Eye Surgery",
      },
      {
        id: 4,
        title: "Prescription",
        value: "Benzocaine, Lidocaine, Mepivacaine, Prilocaine",
      },
    ],
    attachments: [
      "https://placehold.it/300x300",
      "https://placehold.it/300x300",
      "https://placehold.it/300x300",
      "https://placehold.it/300x300",
    ],
    vitalSigns: [
      "Weight: 60 kg",
      "Height: 170 cm",
      "BMI: 20.76 kg/m2",
      "Blood Pressure: 120/80 mmHg",
    ],
  },
  {
    id: 3,
    date: "20, Mar 2022",
    amount: 500000,
    data: [
      {
        id: 1,
        title: "Complaint",
        value: "Painful eyes,Flashing lights and floaters,Blurred vision",
      },
      {
        id: 2,
        title: "Diagnosis",
        value: "Cataracts, Glaucoma, Diabetic eye disease",
      },
      {
        id: 3,
        title: "Treatment",
        value: "Paeditaric Ophthalmology,Drooping Eyelids, Laser Eye Surgery",
      },
      {
        id: 4,
        title: "Prescription",
        value: "Gingival Gel, Chlorhexidine, Fluoride, Calcium",
      },
    ],
    attachments: [
      "https://placehold.it/300x300",
      "https://placehold.it/300x300",
      "https://placehold.it/300x300",
      "https://placehold.it/300x300",
    ],
    vitalSigns: [
      "Temperature: 36.5 °C",
      "Oxygen Saturation: 98%",
      "Blood Pressure: 120/80 mmHg",
      "Pulse Rate: 80 bpm",
      "Respiratory Rate: 16 bpm",
    ],
  },
  {
    id: 4,
    date: "10, Apr 2022",
    amount: 760000,
    data: [
      {
        id: 1,
        title: "Complaint",
        value: "Gradual loss of vision,Headache,Vision problems",
      },
      {
        id: 2,
        title: "Diagnosis",
        value: "Cataracts, Glaucoma, Diabetic eye disease, Hypertension",
      },
      {
        id: 3,
        title: "Treatment",
        value: "Cataracts Surgery, Laser Eye Surgery, Paeditaric Ophthalmology",
      },
      {
        id: 4,
        title: "Prescription",
        value: "Tramadol, Codeine, Morphine, Oxycodone",
      },
    ],
    attachments: [
      "https://placehold.it/300x300",
      "https://placehold.it/300x300",
      "https://placehold.it/300x300",
      "https://placehold.it/300x300",
    ],
    vitalSigns: [
      "Sugar Level: 120 mg/dL",
      "Oxygen Saturation: 98%",
      "Cholesterol: 200 mg/dL",
      "Blood Pressure: 120/80 mmHg",
    ],
  },
];

export const doctorsData = [
  {
    id: 1,
    user: memberData[0],
    title: "Dr.",
  },
  {
    id: 2,
    user: memberData[1],
    title: "Dr.",
  },
  {
    id: 3,
    user: memberData[2],
    title: "Dr.",
  },
  {
    id: 4,
    user: memberData[3],
    title: "Dr.",
  },
];

export const receptionsData = [
  {
    id: 1,
    user: memberData[6],
    title: "Dr.",
  },
  {
    id: 2,
    user: memberData[7],
    title: "Dr.",
  },
  {
    id: 3,
    user: memberData[5],
    title: "Dr.",
  },
  {
    id: 4,
    user: memberData[4],
    title: "Dr.",
  },
  {
    id: 5,
    user: memberData[2],
    title: "Dr.",
  },
  {
    id: 6,
    user: memberData[1],
    title: "Dr.",
  },
];

export const patientImages = [
  "https://res.cloudinary.com/ds5bmx4ee/image/upload/v1711607746/Eye%20Clinic%20Dashboard/2_g7b8yh.jpg",
  "https://res.cloudinary.com/ds5bmx4ee/image/upload/v1711607745/Eye%20Clinic%20Dashboard/3_hz4vrd.webp",
  "https://res.cloudinary.com/ds5bmx4ee/image/upload/v1711607746/Eye%20Clinic%20Dashboard/4_mpyrax.jpg",
  "https://res.cloudinary.com/ds5bmx4ee/image/upload/v1711607748/Eye%20Clinic%20Dashboard/5_ezdsku.webp",
  "https://res.cloudinary.com/ds5bmx4ee/image/upload/v1711607746/Eye%20Clinic%20Dashboard/6_iqoxxa.jpg",
  "https://res.cloudinary.com/ds5bmx4ee/image/upload/v1711607746/Eye%20Clinic%20Dashboard/7_yg4sbv.jpg",
  "https://res.cloudinary.com/ds5bmx4ee/image/upload/v1711607752/Eye%20Clinic%20Dashboard/8_joyhf7.png",
  "https://res.cloudinary.com/ds5bmx4ee/image/upload/v1711607749/Eye%20Clinic%20Dashboard/9_zmsbil.jpg",
  "https://res.cloudinary.com/ds5bmx4ee/image/upload/v1711607746/Eye%20Clinic%20Dashboard/1_uhqkrg.jpg",
];

export const reviewData = [
  {
    id: 1,
    user: memberData[0],
    star: 4,
    comment:
      "Quick appointment scheduling and knowledgeable optometrists.Great service, friendly staff, and thorough eye exams!",
    reviewAbout: {
      name: "Hospital",
      link: "#",
    },
    date: "29 May 2021",
  },
  {
    id: 2,
    user: memberData[1],
    star: 5,
    comment:
      "Great service, friendly staff, and thorough eye exams!,Clean facility, but felt a bit rushed during my appointment",
    reviewAbout: {
      name: `Dr. ${memberData[1].title}`,
      link: "/doctors/preview/1",
    },
    date: "12 Jan 2021",
  },
  {
    id: 3,
    user: memberData[2],
    star: 2,
    comment:
      "Best product ever this clinic is best for providing the best service. I recommend it",
    reviewAbout: {
      name: `Product: Sunglasses`,
      link: "/",
    },
    date: "04 Aug 2021",
  },
  {
    id: 4,
    user: memberData[3],
    star: 5,
    comment:
      "Great service, friendly staff, and thorough eye exams!,Clean facility, but felt a bit rushed during my appointment",
    reviewAbout: {
      name: `Dr. ${memberData[3].title}`,
      link: "/doctors/preview/3",
    },
    date: "12 Jan 2021",
  },
  {
    id: 5,
    user: memberData[4],
    star: 3,
    comment:
      "Quick appointment scheduling and knowledgeable optometrists.Great service, friendly staff, and thorough eye exams!",
    reviewAbout: {
      name: "Hospital",
      link: "#",
    },
    date: "04 Aug 2021",
  },
  {
    id: 6,
    user: memberData[5],
    star: 0,
    comment:
      "I use the product but it give me eye problems. I will not use this product again.",
    reviewAbout: {
      name: `Product: Single vision`,
      link: "/",
    },
    date: "09 Apr 2021",
  },
];

export const chatsData = [
  {
    id: 1,
    user: memberData[0],
    active: "2 min ago",
    status: true,
    message: "Appointment delay doctor..",
  },
  {
    id: 2,
    user: memberData[1],
    active: "2:30 Pm",
    status: true,
    message: "Can we have meeting now??",
  },
  {
    id: 3,
    user: memberData[2],
    active: "1:30 Pm",
    status: true,
    message: "i need your help doctor",
  },
  {
    id: 4,
    user: memberData[3],
    active: "Yesterday",
    status: true,
    message: "How are you doing??",
  },
  {
    id: 5,
    user: memberData[4],
    active: "12/4/2024",
    status: false,
    message: "Delete all patient data",
  },
  {
    id: 6,
    user: memberData[5],
    active: "11/4/2024",
    status: false,
    message: "Hellow doctor..",
  },
  {
    id: 7,
    user: memberData[6],
    active: "06/4/2024",
    status: false,
    message: "Need your minute. are you available?    ",
  },
  {
    id: 8,
    user: memberData[7],
    active: "05/3/2024",
    status: false,
    message: "Morning.",
  },

  {
    id: 9,
    user: memberData[0],
    active: "11/4/2024",
    status: false,
    message: "Hellow doctor..",
  },
  {
    id: 10,
    user: memberData[3],
    active: "06/4/2024",
    status: false,
    message: "Need your minute. are you available?    ",
  },
  {
    id: 11,
    user: memberData[1],
    active: "05/3/2024",
    status: false,
    message: "Morning.",
  },
];

export const convData = [
  {
    id: 1,
    user: memberData[0],
    text: "Morning dr. Daudi 👐👐",
    time: "12:00 PM",
    imageUrl: "",
    value: {
      image: false,
      me: false,
    },
  },
  {
    id: 2,
    user: memberData[4],
    text: "Morning how are you doing",
    time: "12:02 PM",
    imageUrl: "",
    value: {
      image: false,
      me: true,
    },
  },
  {
    id: 3,
    user: memberData[0],
    text: "Im doing well.. is patient 23 room available",
    time: "12:05 PM",
    imageUrl: "",
    value: {
      image: false,
      me: false,
    },
  },
  {
    id: 4,
    user: memberData[0],
    text: "I need to make appointment with her",
    time: "12:05 PM",
    imageUrl: "",
    value: {
      image: false,
      me: false,
    },
  },
  {
    id: 5,
    user: memberData[4],
    text: "She is available dear..",
    time: "01:06 PM",
    imageUrl: "",
    value: {
      image: false,
      me: true,
    },
  },
  {
    id: 6,
    user: memberData[0],
    text: "Ohh thank you 😌😌😌",
    time: "01:09 PM",
    imageUrl: "",
    value: {
      image: false,
      me: false,
    },
  },
  {
    id: 7,
    user: memberData[4],
    text: "Check out her image...",
    time: "01:14 PM",
    imageUrl: "",
    value: {
      image: false,
      me: true,
    },
  },
  {
    id: 8,
    user: memberData[4],
    text: "",
    time: "01:14 PM",
    imageUrl:
      "https://res.cloudinary.com/ds5bmx4ee/image/upload/v1711607745/Eye%20Clinic%20Dashboard/3_hz4vrd.webp",
    value: {
      image: true,
      me: true,
    },
  },
  {
    id: 9,
    user: memberData[0],
    text: "I will check on her account 😌",
    time: "01:18 PM",
    imageUrl: "",
    value: {
      image: false,
      me: false,
    },
  },
];
