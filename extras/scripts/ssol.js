// used for getting the enrollment data from SSOL

// based on
// https://www.geeksforgeeks.org/how-to-export-html-table-to-csv-using-javascript/

const downloadCSVFile = (csvData) => {
  const CSVFile = new Blob([csvData], {
    type: "text/csv",
  });

  // Create to temporary link to initiate download process
  const tempLink = document.createElement("a");

  // Download csv file
  const title = document.getElementsByTagName("h3")[0].innerText;
  const now = new Date();
  tempLink.download = `${title} - ${now.toISOString()}.csv`;
  const url = URL.createObjectURL(CSVFile);
  tempLink.href = url;

  // This link should not be displayed
  tempLink.style.display = "none";
  document.body.appendChild(tempLink);

  // Automatically click the link to trigger download
  tempLink.click();
  document.body.removeChild(tempLink);
};

const tableToCSV = () => {
  const csvData = [];

  const rows = document.getElementsByTagName("tr");
  for (const row of rows) {
    const cols = row.querySelectorAll("td,th");
    const csvrow = [];
    for (const col of cols) {
      csvrow.push(col.innerText);
    }

    csvData.push(csvrow.join(","));
  }

  downloadCSVFile(csvData.join("\n"));
};

tableToCSV();
