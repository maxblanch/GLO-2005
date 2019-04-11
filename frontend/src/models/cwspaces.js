import cwspace from "./cwspace";

const cwspaces = {
  from: cwspacesData =>
    cwspacesData.map(cwspaceData => cwspace.from(cwspaceData))
};

export default cwspaces;
