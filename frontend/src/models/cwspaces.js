import cwspace from "./cwspace";

const cwspaces = {
  from: cwspacesData =>
    cwspacesData.map(cwspaceData => cwspace.from(cwspaceData)),

  fromManager: (cwspacesData, managerId) =>
    cwspacesData.map(cwspaceData => {
      const space = cwspace.from(cwspaceData);
      if (space.managerId === managerId) return space;
    })
};

export default cwspaces;
