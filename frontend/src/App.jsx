import React, { useState } from "react";
import "./App.css";

const formatINRCurrency = (amount) =>
  new Intl.NumberFormat("en-IN", {
    style: "currency",
    currency: "INR",
    maximumFractionDigits: 2,
  }).format(amount);

function App() {
  const [formData, setFormData] = useState({
    project_type: "Web Application",
    client_industry: "Finance",
    estimated_timeline_months: "5",
    team_allocation: "6",
    complexity_score: "3",
    revision_count: "2",
  });

  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const projectTypes = [
    "Web Application",
    "Mobile Application",
    "AI/ML Solution",
    "ERP System",
    "CRM System",
    "DevOps Automation",
    "Cloud Migration",
    "Cybersecurity Implementation",
    "Data Engineering Pipeline",
    "Business Intelligence Dashboard",
    "IoT System",
    "Blockchain Solution",
    "E-commerce Platform",
    "SaaS Product",
    "Legacy System Modernization",
  ];

  const clientIndustries = [
    "Finance",
    "Healthcare",
    "Retail",
    "Education",
    "Startup",
  ];

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({
      ...prev,
      [name]: value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const response = await fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          project_type: formData.project_type,
          client_industry: formData.client_industry,
          estimated_timeline_months: parseInt(
            formData.estimated_timeline_months
          ),
          team_allocation: parseInt(formData.team_allocation),
          complexity_score: parseInt(formData.complexity_score),
          revision_count: parseInt(formData.revision_count),
        }),
      });

      const data = await response.json();

      if (data.success) {
        setResult({
          predicted_cost: data.predicted_cost,
          message: data.message,
        });
      } else {
        setError(data.error || "Failed to get prediction");
      }
    } catch (err) {
      setError(
        err.message || "Unable to connect to the backend. Is it running?"
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app-wrapper">
      <section className="estimator-section">
        <div className="estimator-container">
          <form onSubmit={handleSubmit} className="prediction-form">
            <div className="form-section">
              <h2>Project Details</h2>

              <div className="form-group">
                <label htmlFor="project_type">Project Type</label>
                <select
                  id="project_type"
                  name="project_type"
                  value={formData.project_type}
                  onChange={handleChange}
                  required
                >
                  {projectTypes.map((type) => (
                    <option key={type} value={type}>
                      {type}
                    </option>
                  ))}
                </select>
              </div>

              <div className="form-group">
                <label htmlFor="client_industry">Client Industry</label>
                <select
                  id="client_industry"
                  name="client_industry"
                  value={formData.client_industry}
                  onChange={handleChange}
                  required
                >
                  {clientIndustries.map((industry) => (
                    <option key={industry} value={industry}>
                      {industry}
                    </option>
                  ))}
                </select>
              </div>
            </div>

            <div className="form-section">
              <h2>Project Specifications</h2>

              <div className="form-row">
                <div className="form-group">
                  <label htmlFor="estimated_timeline_months">
                    Timeline (months)
                  </label>
                  <input
                    type="number"
                    id="estimated_timeline_months"
                    name="estimated_timeline_months"
                    value={formData.estimated_timeline_months}
                    onChange={handleChange}
                    min="1"
                    max="36"
                    required
                  />
                </div>

                <div className="form-group">
                  <label htmlFor="team_allocation">Team Size</label>
                  <input
                    type="number"
                    id="team_allocation"
                    name="team_allocation"
                    value={formData.team_allocation}
                    onChange={handleChange}
                    min="1"
                    max="20"
                    required
                  />
                </div>
              </div>

              <div className="form-row">
                <div className="form-group">
                  <label htmlFor="complexity_score">
                    Complexity (1-5)
                  </label>
                  <input
                    type="number"
                    id="complexity_score"
                    name="complexity_score"
                    value={formData.complexity_score}
                    onChange={handleChange}
                    min="1"
                    max="5"
                    required
                  />
                </div>

                <div className="form-group">
                  <label htmlFor="revision_count">Revision Count</label>
                  <input
                    type="number"
                    id="revision_count"
                    name="revision_count"
                    value={formData.revision_count}
                    onChange={handleChange}
                    min="0"
                    max="15"
                    required
                  />
                </div>
              </div>
            </div>

            <button type="submit" className="submit-btn" disabled={loading}>
              {loading ? "Calculating..." : "Predict Cost"}
            </button>
          </form>

          {error && (
            <div className="alert alert-error">
              <strong>Error:</strong> {error}
            </div>
          )}

          {result && (
            <div className="alert alert-success">
              <h3>Prediction Result</h3>
              <p className="cost-display">
                Estimated Cost: <span className="cost-amount">{formatINRCurrency(result.predicted_cost)}</span>
              </p>
              <p className="message">{result.message}</p>
            </div>
          )}
        </div>
      </section>
    </div>
  );
}

export default App;