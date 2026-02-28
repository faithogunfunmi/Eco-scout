import { useState } from 'react';
import { Leaf, Search } from 'lucide-react';
import { MOCK_CASES, DEFAULT_RECOMMENDATIONS} from './brandData';
import './App.css';

const translateRating = (number) => {
  if (number === 0) return "Yes";
  if (number === 1) return "No";
  if (number === 2) return "Mixed";
  return "Unknown";
};

function App() {
  const [activeView, setActiveView] = useState('default');
  // Grab the data for the selected brand (will be null if 'default' is active)
  const brandData = activeView !== 'default' ? MOCK_CASES[activeView] : null;

  return (
    <div className="app-container">
      {/* HEADER */}
      <header className="header">
        <Leaf size={24} color="#16a34a" />
        <h1>EcoScout</h1>
      </header>

      {/* --- THE DEFAULT VIEW --- */}
      {activeView === 'default' && (
        <div className="view-container">
          <h2>Scouting for a greener planet.</h2>
          <p className="subtitle">We didn't detect a fast-fashion brand here. Here are some of our favorite sustainable options:</p>
          
          <div className="rec-list">
            {DEFAULT_RECOMMENDATIONS.map((rec, idx) => (
              <div key={idx} className="rec-card">
                <h3>{rec.name}</h3>
                <span className="tag">{rec.type}</span>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* --- THE BRAND VIEWS (Yes, Mixed, No) --- */}
      {activeView !== 'default' && brandData && (
        <div className="view-container">
          <h2 className="brand-title">{brandData.name}</h2>
          
          {/* Ratings Section */}
          <div className="ratings-box">
            <div className="rating-row">
              <span>Ethics Rating:</span>
              <strong>{translateRating(brandData.ethics)}</strong>
            </div>
            <div className="rating-row">
              <span>Sustainability Rating:</span>
              <strong>{translateRating(brandData.sustainability)}</strong>
            </div>
          </div>

          {/* The Visual Meter */}
          <div className="meter-section">
            <div className="meter-container">
              <div className={`meter-arc ${brandData.overall}`}></div>
              <div className={`meter-needle point-${brandData.overall}`}></div>
            </div>
            <div className="meter-labels">
              <span>Yes</span>
              <span>Mixed</span>
              <span>No</span>
            </div>
          </div>

          {/* Recommendations Box (Only show if there are recommendations) */}
          {brandData.recommendations.length > 0 && (
            <div className="rec-box">
              <h3>Recommendations</h3>
              <div className="rec-tags">
                {brandData.recommendations.map((rec, idx) => (
                  <span key={idx} className="rec-pill">{rec}</span>
                ))}
              </div>
            </div>
          )}
        </div>
      )}

      {/* --- HACKATHON TEST BUTTONS (We will delete these later) --- */}
      <div className="test-panel">
        <p>Test Views:</p>
        <div className="test-buttons">
          <button onClick={() => setActiveView('default')} className={activeView === 'default' ? 'active' : ''}>Default</button>
          <button onClick={() => setActiveView('yes')} className={activeView === 'yes' ? 'active' : ''}>Yes</button>
          <button onClick={() => setActiveView('mixed')} className={activeView === 'mixed' ? 'active' : ''}>Mixed</button>
          <button onClick={() => setActiveView('no')} className={activeView === 'no' ? 'active' : ''}>No</button>
        </div>
      </div>
    </div>
  );
}

export default App;
