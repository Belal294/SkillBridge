// App.jsx
import './App.css';
import { AuthProvider } from './context/AuthContext';
import AppRoutes from './routes/AppRoutes';
import { BrowserRouter } from 'react-router-dom';

function App() {
  return (
    <AuthProvider>
    <BrowserRouter>
      <AppRoutes />
    </BrowserRouter>
    </AuthProvider>
  );
}

export default App;
