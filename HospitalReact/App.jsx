import './App.css'
import {Suspense, lazy} from 'react'
import {BrowserRouter, Route, Routes} from 'react-router-dom'
import Aos from 'aos'
import Toast from './src/components/Notifications/Toast'
import BigLoader from './src/components/Notifications/BigLoader'

const Dashboard = lazy(() => import('./src/screens/Dashboard'))
const Payments = lazy(() => import('./src/screens/Payments/Payments'))
const Appointments = lazy(() => import('./src/screens/Appointments'))
const Patients = lazy(() => import('./src/screens/Patients/Patients'))
const Campaings = lazy(() => import('./src/screens/Campaings'))
const Procedures = lazy(() => import('./src/screens/Procedures'))
const Invoices = lazy(() => import('./src/screens/Invoices/Invoices'))
const Settings = lazy(() => import('./src/screens/Settings'))
const CreateInvoice = lazy(() => import('./src/screens/Invoices/CreateInvoice'))
const EditInvoice = lazy(() => import('./src/screens/Invoices/EditInvoice'))
const PreviewInvoice = lazy(() =>
    import('./src/screens/Invoices/PreviewInvoice')
)
const EditPayment = lazy(() => import('./src/screens/Payments/EditPayment'))
const PreviewPayment = lazy(() =>
    import('./src/screens/Payments/PreviewPayment')
)
const Medicine = lazy(() => import('./src/screens/Medicine'))
const DiagnosticAid = lazy(() => import('./src/screens/DiagnosticAid'))
const PatientProfile = lazy(() =>
    import('./src/screens/Patients/PatientProfile')
)
const CreatePatient = lazy(() => import('./src/screens/Patients/CreatePatient'))
const Doctors = lazy(() => import('./src/screens/Persons/Persons.jsx'))
const DoctorProfile = lazy(() => import('./src/screens/Persons/DoctorProfile'))
const Receptions = lazy(() => import('./src/screens/Receptions'))
const NewMedicalRecode = lazy(() =>
    import('./src/screens/Patients/NewMedicalRecode')
)


const NotFound = lazy(() => import('./src/screens/NotFound'))
const Login = lazy(() => import('./src/screens/Login'))
const Reviews = lazy(() => import('./src/screens/Reviews'))
const Chats = lazy(() => import('./src/screens/Chats/Chats'))

function App() {
    Aos.init()

    return (
        <>
            {/* Toaster */}
            <Toast/>
            {/* Routes */}
            <BrowserRouter>
                <Routes>
                    <Route
                        path='/'
                        element={
                            <Suspense fallback={<BigLoader/>}>
                                <Dashboard/>
                            </Suspense>
                        }
                    />
                    {/* invoce */}
                    <Route
                        path='/invoices'
                        element={
                            <Suspense fallback={<BigLoader/>}>
                                <Invoices/>
                            </Suspense>
                        }
                    />
                    <Route
                        path='/invoices/create'
                        element={
                            <Suspense fallback={<BigLoader/>}>
                                <CreateInvoice/>
                            </Suspense>
                        }
                    />
                    <Route
                        path='/invoices/edit/:id'
                        element={
                            <Suspense fallback={<BigLoader/>}>
                                <EditInvoice/>
                            </Suspense>
                        }
                    />
                    <Route
                        path='/invoices/preview/:id'
                        element={
                            <Suspense fallback={<BigLoader/>}>
                                <PreviewInvoice/>
                            </Suspense>
                        }
                    />
                    {/* payments */}
                    <Route
                        path='/payments'
                        element={
                            <Suspense fallback={<BigLoader/>}>
                                <Payments/>
                            </Suspense>
                        }
                    />
                    <Route
                        path='/payments/edit/:id'
                        element={
                            <Suspense fallback={<BigLoader/>}>
                                <EditPayment/>
                            </Suspense>
                        }
                    />
                    <Route
                        path='/payments/preview/:id'
                        element={
                            <Suspense fallback={<BigLoader/>}>
                                <PreviewPayment/>
                            </Suspense>
                        }
                    />
                    {/* patient */}
                    <Route
                        path='/patients'
                        element={
                            <Suspense fallback={<BigLoader/>}>
                                <Patients/>
                            </Suspense>
                        }
                    />
                    <Route
                        path='/patients/preview/:id'
                        element={
                            <Suspense fallback={<BigLoader/>}>
                                <PatientProfile/>
                            </Suspense>
                        }
                    />
                    <Route
                        path='/patients/create'
                        element={
                            <Suspense fallback={<BigLoader/>}>
                                <CreatePatient/>
                            </Suspense>
                        }
                    />
                    <Route
                        path='/patients/visiting/:id'
                        element={
                            <Suspense fallback={<BigLoader/>}>
                                <NewMedicalRecode/>
                            </Suspense>
                        }
                    />
                    {/* doctors */}
                    <Route
                        path='/employees'
                        element={
                            <Suspense fallback={<BigLoader/>}>
                                <Doctors/>
                            </Suspense>
                        }
                    />
                    <Route
                        path='/doctors/preview/:id'
                        element={
                            <Suspense fallback={<BigLoader/>}>
                                <DoctorProfile/>
                            </Suspense>
                        }
                    />
                    {/* reception */}
                    <Route
                        path='/receptions'
                        element={
                            <Suspense fallback={<BigLoader/>}>
                                <Receptions/>
                            </Suspense>
                        }
                    />
                    {/* others */}
                    <Route
                        path='/login'
                        element={
                            <Suspense fallback={<BigLoader/>}>
                                <Login/>
                            </Suspense>
                        }
                    />
                    <Route
                        path='/appointments'
                        element={
                            <Suspense fallback={<BigLoader/>}>
                                <Appointments/>
                            </Suspense>
                        }
                    />
                    <Route
                        path='/campaigns'
                        element={
                            <Suspense fallback={<BigLoader/>}>
                                <Campaings/>
                            </Suspense>
                        }
                    />
                    <Route
                        path='/medicine'
                        element={
                            <Suspense fallback={<BigLoader/>}>
                                <Medicine/>
                            </Suspense>
                        }
                    />
                    <Route
                        path='/procedures'
                        element={
                            <Suspense fallback={<BigLoader/>}>
                                <Procedures/>
                            </Suspense>
                        }
                    />
                    <Route
                        path='/diagnosticaids'
                        element={
                            <Suspense fallback={<BigLoader/>}>
                                <DiagnosticAid/>
                            </Suspense>
                        }
                    />
                    <Route
                        path='/settings'
                        element={
                            <Suspense fallback={<BigLoader/>}>
                                <Settings/>
                            </Suspense>
                        }
                    />
                    <Route
                        path='*'
                        element={
                            <Suspense fallback={<BigLoader/>}>
                                <NotFound/>
                            </Suspense>
                        }
                    />
                </Routes>
            </BrowserRouter>
        </>
    )
}

export default App
