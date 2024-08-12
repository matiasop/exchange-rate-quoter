import _ from "lodash";

export const transformToSnakeCase = (
  obj: Record<string, any>
): Record<string, any> => {
  return _.mapKeys(obj, (value, key) => _.snakeCase(key));
};

export const transformToCamelCase = <T>(obj: Record<string, any>): T => {
  return _.mapKeys(obj, (value, key) => _.camelCase(key)) as T;
};
